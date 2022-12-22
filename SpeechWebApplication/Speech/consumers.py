import json
from channels.consumer import SyncConsumer, AsyncConsumer
from vosk import Model, KaldiRecognizer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):

        print('Websocket Connected...', event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):

        print('Message Received...', event)
        print('Message is', event['text'])
        for i in range(50):
            self.send({
                'type': 'websocket.send',
                'text': str(i)
            })

    def websocket_disconnect(self, event):

        print('Websocket Disconnected...', event)


class MyAsyncConsumer(AsyncConsumer):
    global model
    global recognizer
    #model = Model(model_name="vosk-model-small-hi-0.22")
    model = Model(model_name="vosk-model-small-en-us-0.15")
    #model = Model("./Speech/model/vosk-model-en-us-0.42-gigaspeech")
    recognizer = KaldiRecognizer(model, 16000)
    recognizer.SetWords(True)

    async def websocket_connect(self, event):
        # file = open('./static/para.txt', 'r')
        # for book_input in file:
        #     print (book_input)
        print('Websocket Connected...', event)
        await self.send({
            'type': 'websocket.accept'
        })
        # await self.send({
        #     'type': 'websocket.send',
        #     'text': book_input,
	    #     'code': 'input'
        # })

    async def websocket_receive(self, event):
        # data=json.dump(event['bytes'])
        data=event['bytes']
        recognizer.AcceptWaveform(data)
        text = recognizer.Result()
        results = json.loads(text)["text"]

        await self.send({
            'type': 'websocket.send',
            'text': results,
	        'code': 'output'
        })

    async def websocket_disconnect(self, event):
        if event =='{"eof" : 1}':
            print('Websocket Disconnected...', event)

