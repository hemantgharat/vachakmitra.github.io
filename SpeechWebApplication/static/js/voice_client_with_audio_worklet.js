var context;
var source;
var processor;
var streamLocal;
var webSocket;
var inputArea;
const sampleRate = 12000;
const wsURL = 'ws://127.0.0.1:8000/ws/ac/';
var initComplete = false;
(function () {
    document.addEventListener('DOMContentLoaded', (event) => {
        inputArea = document.getElementById('q');

        const listenButton = document.getElementById('listen');
        const stopListeningButton = document.getElementById('stopListening');

        listenButton.addEventListener('mousedown', function () {
            listenButton.disabled = true;
            MediaStreamTrack
            initWS();
            navigator.mediaDevices.getUserMedia({
                audio: {
                    echoCancellation: !1,
                    autoGainControl: !1,
                    noiseSuppression: !1,
                    channelCount: 1,
                    sampleRate
                }, video: false
            }).then(handleSuccess);
            listenButton.style.color = 'green';
            initComplete = true;
        });

        stopListeningButton.addEventListener('mouseup', function () {
            if (initComplete === true) {

            webSocket.send('{"eof" : 1}');
            webSocket.close();
            console.log('Disconnected...');

            processor.port.close();
            source.disconnect(processor);
            context.close();

            if (streamLocal.active) {
                streamLocal.getTracks()[0].stop();
            }
            listenButton.style.color = 'black';
                listenButton.disabled = false;
                initComplete = false;
                inputArea.innerText = ""
            }
        });

    });
}())


const handleSuccess = function (stream) {
    streamLocal = stream;
    context = new AudioContext({sampleRate: sampleRate});

    context.audioWorklet.addModule('static/js/data-conversion-processor.js').then(
        function () {
            processor = new AudioWorkletNode(context, 'data-conversion-processor', {
                
            numberOfInputs: 1,
            numberOfOutputs: 1,
            outputChannelCount: [1],
            parameterData: {},
            });


            let constraints = {audio: true};
            navigator.mediaDevices.getUserMedia(constraints).then(function (stream) {
                source = context.createMediaStreamSource(stream);
                
                source.connect(processor);
                processor.connect(context.destination);

                processor.port.onmessage = event => webSocket.send(event.data)
                processor.port.start()
            });
        }
    );
};

function initWS() {
    webSocket = new WebSocket(wsURL);
    webSocket.binaryType = "arraybuffer";

    webSocket.onopen = function (event) {
        console.log('New connection established');
        // document.getElementById("q").innerText=event.data;
        console.log(event);
    };

    webSocket.onerror = function (event) {
        console.error(event.data);
    };

    webSocket.onmessage = function (event) {
        if (event.data) {
            //document.getElementById("ip").innerText=event.data
            document.getElementById("q").innerText=event.data;
            console.log(event.data);
            // let parsed = JSON.parse(event.data);
            // if (parsed.result) console.log(parsed.result);
            // if (parsed.text) inputArea.innerText = parsed.text;
        }
    };
}
