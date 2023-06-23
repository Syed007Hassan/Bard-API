from bardapi import Bard


class ResponseService:
    def __init__(self, api_key):
        self.bard = Bard(api_key)

    def create_response(self, prompt):
        prompt1 = "You are a professional Chatbot integrated into ONE Technology Services' website, a software company offering a wide range of software services. Your role is to provide concise and informative information about the company's services. If users wish to contact the company, they can do so through LinkedIn (https://www.linkedin.com/company/one-technology-services/), Twitter (https://twitter.com/ONETechnologySer) and can email us on our email ""info@onetechnologyservices.com"". Please provide a response to the following question regarding ONE Technology Services' software services.Here is the question: "

        try:
            # Use Bard to get an answer to the prompt
            answer = self.bard.get_answer(prompt1 + prompt)['content']
            return answer
        except Exception as e:
            raise Exception(f"Failed to get answer from Bard API: {str(e)}")
