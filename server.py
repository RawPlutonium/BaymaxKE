# coding: utf-8
from messengerbot import MessengerClient, messages, attachments, templates, elements
import warnings
import os
from fbmq import Attachment, Template, QuickReply, Page
from flask import Flask, request

FACEBOOK_TOKEN = 'EAARoG7uz7ZA0BAKS0PJs4E6YyPZCm4Wj0C2eiTKZCjuF76j345I6EdFxMS6KUxZCh6bgZCx8ZCcqfxwxVJtsecPhjLbdI4Hs9dQZBLYjmGyd9bHUbDrPyeFHniH5T2RtI8WsGF5IShgXrNjsZBVEGgZAyt2yWRgh1j11K9NnVfxGA9QZDZD'
from pymessenger.bot import Bot

app = Flask(__name__)

VERIFY_TOKEN = '90293'
bot = Bot(FACEBOOK_TOKEN)

messenger = MessengerClient(access_token=FACEBOOK_TOKEN)

# With env var export MESSENGER_PLATFORM_ACCESS_TOKEN=your_token



@app.route('/verify', methods=['GET'])
def verify():
    if request.args.get('hub.verify_token', '') == '90293':
        return request.args.get('hub.challenge', '')
    else:
        return 'Error, wrong validation token'

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
        print output
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                recipient_id = x['sender']['id']
                postback_button1 = elements.PostbackButton(
                   title='Good',
                   payload='USER_DEFINED_PAYLOAD'
                )
                postback_button2 = elements.PostbackButton(
                   title='Kinda Sick',
                   payload='USER_DEFINED_PAYLOAD2'
                )
                postback_button3 = elements.PostbackButton(
                   title='Headache',
                   payload='USER_DEFINED_PAYLOAD3'
                )
                postback_button4 = elements.PostbackButton(
                   title='Stomachache',
                   payload='USER_DEFINED_PAYLOAD4'
                )
                postback_button5 = elements.PostbackButton(
                   title='Cough',
                   payload='USER_DEFINED_PAYLOAD5'
                )
                postback_button6 = elements.PostbackButton(
                   title='Diarrhoea',
                   payload='USER_DEFINED_PAYLOAD6'
                )
                postback_button7 = elements.PostbackButton(
                   title='Dry',
                   payload='USER_DEFINED_PAYLOAD7'
                )
                postback_button8 = elements.PostbackButton(
                   title='Wet',
                   payload='USER_DEFINED_PAYLOAD8'
                )
                postback_button9 = elements.PostbackButton(
                   title='Long',
                   payload='USER_DEFINED_PAYLOAD6'
                )
                postback_button10 = elements.PostbackButton(
                   title='Short',
                   payload='USER_DEFINED_PAYLOAD6'
                )

                template1 = templates.ButtonTemplate(
                   text='How are you feeling now?',
                   buttons=[

                       postback_button1 , postback_button2
                   ]
                )
                template2 = templates.ButtonTemplate(
                   text="I am sorry, what symptom do you have?",
                   buttons=[
                       postback_button3, postback_button4, postback_button5
                   ]
                )
                template3 = templates.ButtonTemplate(
                   text="Is it a dry or a wet cough?",
                   buttons=[
                       postback_button7,postback_button8
                   ]
                )
                template4 = templates.ButtonTemplate(
                   text="How long has it lasted?",
                   buttons=[
                       postback_button9,postback_button10
                   ]
                )
                attachment1 = attachments.TemplateAttachment(template=template1)
                attachment2 = attachments.TemplateAttachment(template=template2)
                attachment3 = attachments.TemplateAttachment(template=template3)
                attachment4 = attachments.TemplateAttachment(template=template4)
                recipient = messages.Recipient(recipient_id=recipient_id)
                if x.get('message'):

                    if x['message'].get('text'):
                        message = x['message']['text']
                        if message.lower() == 'hi' or message.lower() == 'hello':
                        #send message
                            message = messages.Message(text='Hello I\'m Baymax, your personal healthcare companion')
                            requ = messages.MessageRequest(recipient, message)
                            messenger.send(requ)
                        else:
                            try:
                                number = int(message)
                                if x['message'].get('text'):
                                    message = x['message']['text']
                                    if int(message)>=5:
                                        bot.send_text_message(recipient_id,"Please see a doctor as soon as possible. Before that, go to your local chemist and find paracetamols")
                                    elif int(message)<5:
                                        bot.send_text_message(recipient_id,"Please see a chemist for a paracetamol, Otherwise, warm milk and sleep helps :)")
                                        my_elements  = []
                                        element1 = elements.Element(
                title='paracetamol',
                image_url="https://s.s-bol.com/imgbase0/imagebase/large/FC/2/2/0/7/9200000005137022.jpg",
                subtitle='Paracetamol Actavis',
                buttons=[
                    elements.WebUrlButton(
                        title='View Item',
                        url='https://www.drugs.com/uk/paracetamol-500mg-tablets-leaflet.html',
                    )
                ]
            )
                                        element2 = elements.Element(
title='paracetamol',
image_url='https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwis2fiE5-7SAhUBvhQKHYlTCzoQjRwIBw&url=http%3A%2F%2Fwww.consumer-voice.org%2Fcomparative-product-testing%2FPERSONAL-CARE-PRODUCTS%2FParacetamol-Tablets1998&bvm=bv.150475504,d.d24&psig=AFQjCNHE6zy2u63-aL8KjMGiyiMYBHMH7w&ust=1490433344081063',
subtitle='paracetamol-500mg',
buttons=[
elements.WebUrlButton(
title='View Item',
url='https://www.drugs.com/uk/paracetamol-500mg-tablets-leaflet.html',
)
]
)

                                        my_elements.append(element1)
                                        my_elements.append(element2)
                                        template = templates.GenericTemplate(my_elements)
                                        attachment = attachments.TemplateAttachment(template)
                                        message = messages.Message(attachment=attachment)
                                        req1 = messages.MessageRequest(recipient, message)
                                        messenger.send(req1)
                                    else:
                                        bot.send_text_message(recipient_id,"Sorry, I didn't quite get that")
                                else:
                                    return None
                            except ValueError:
                                pass

                elif x.get('postback'):
                    if x.get('postback').get('payload')== 'USER_DEFINED_PAYLOAD':
                        bot.send_text_message(recipient_id,"Great! Have an apple!")


                    elif x.get('postback').get('payload')== 'USER_DEFINED_PAYLOAD2':
                        attachment2 = attachments.TemplateAttachment(template=template2)
                        message = messages.Message(attachment=attachment2)
                        requer = messages.MessageRequest(recipient, message)
                        messenger.send(requer)

                    elif x.get('postback').get('payload')== 'USER_DEFINED_PAYLOAD3':

                            bot.send_text_message(recipient_id,"On a scale of one to ten, how can you rate your pain?")

                    elif x.get('postback').get('payload')== 'USER_DEFINED_PAYLOAD4':
                            bot.send_text_message(recipient_id,"On a scale of one to ten, how can you rate your pain?")
                    elif x['message'].get('text'):
                                message = x['message']['text']
                                if int(message)>=5:
                                    bot.send_text_message(recipient_id,"Please see a doctor as soon as possible. Before that, go to your local chemist and find some OTC medicine. If Its too expensive please make some by :")
                                elif int(message)<5:
                                    bot.send_text_message(recipient_id,"Please see a chemist for OTC, Otherwise, Warm water and salt helps with a bit of sugar :)")

                                else:
                                    bot.send_text_message(recipient_id,"Sorry, I didn't quite get that")
                    elif x.get('postback').get('payload')== 'USER_DEFINED_PAYLOAD5':
                            attachment3 = attachments.TemplateAttachment(template=template3)
                            message = messages.Message(attachment=attachment3)
                            reqir = messages.MessageRequest(recipient, message)
                            messenger.send(reqir)

                    elif x.get('postback').get('payload')== 'USER_DEFINED_PAYLOAD7':
                                attachment4 = attachments.TemplateAttachment(template=template4)
                                message = messages.Message(attachment=attachment4)
                                reqr = messages.MessageRequest(recipient, message)
                                messenger.send(reqr)

                    elif x.get('postback').get('payload')== 'USER_DEFINED_PAYLOAD9':
                                    bot.send_text_message(recipient_id,"See a doctor Immediately")
                    elif x.get('postback').get('payload')== 'USER_DEFINED_PAYLOAD10':
                                    bot.send_text_message(recipient_id,"Buy Trahistamine From a chemist")

                    elif x.get('postback').get('payload')== 'USER_DEFINED_PAYLOAD8':
                                attachment4 = attachments.TemplateAttachment(template=template4)
                                message = messages.Message(attachment=attachment4)
                                reqr = messages.MessageRequest(recipient, message)
                                messenger.send(reqr)

                                if x.get('postback').get('payload')== 'USER_DEFINED_PAYLOAD9':
                                    bot.send_text_message(recipient_id,"See a doctor Immediately")
                                elif x.get('postback').get('payload')== 'USER_DEFINED_PAYLOAD10':
                                    bot.send_text_message(recipient_id,"Buy Trahistamine From a chemist")
                    elif x.get('postback').get('payload')== 'USER_DEFINED_PAYLOAD6':
                            attachment4 = attachments.TemplateAttachment(template=template4)
                            message = messages.Message(attachment=attachment4)
                            reqr = messages.MessageRequest(recipient, message)
                            messenger.send(reqr)

                    elif x.get('postback').get('payload')== 'USER_DEFINED_PAYLOAD9':
                                bot.send_text_message(recipient_id,"See a doctor Immediately")
                    elif x.get('postback').get('payload')== 'USER_DEFINED_PAYLOAD10':
                                bot.send_text_message(recipient_id,"Drink Lots of water and ORS")






                    else:
                        bot.send_text_message(recipient_id,"Sorry, I didn't quite get that.")






















                    pass
    return "Success"

if __name__ == '__main__':
    # Suppress nltk warnings about not enough data
    warnings.filterwarnings('ignore', '.*returning an arbitrary sample.*',)

    if os.path.exists("corpus.txt"):
        bot = chatbot.Bot(open("corpus.txt").read())

    app.run(port=3000, debug=True)
