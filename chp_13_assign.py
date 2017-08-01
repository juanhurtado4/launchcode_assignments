class BoredChatbot(Chatbot):
    def response(self, prompt_from_human):
        if len(prompt_from_human) >= 20:
            return 'zzz... Oh excuse me, I dozed off reading your essay.'
        else:
            return "It is very interesting that you say: '" + prompt_from_human + "'"