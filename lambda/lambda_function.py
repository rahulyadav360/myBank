from ask_sdk_core.dispatch_components import (AbstractRequestHandler, AbstractExceptionHandler, AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name, get_supported_interfaces

from ask_sdk_model.interfaces.alexa.presentation.apl import (
    RenderDocumentDirective, ExecuteCommandsDirective, SpeakItemCommand, HighlightMode
)

import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def supports_apl(handler_input):

    supported_interfaces = get_supported_interfaces(
        handler_input)
    return supported_interfaces.alexa_presentation_apl != None

def _load_apl_document(file_path):

    with open(file_path) as f:
        logger.debug(f)
        return json.load(f)

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)
        
    def handle(self, handler_input):
        logger.info("In LaunchRequestHandler")
        
        session_attributes = handler_input.attributes_manager.session_attributes
        speech_output = "Hey there! I am your home insurance agent. Ask me any questions that you have about a home insurance policy."
        reprompt = "What do you want to ask?"
        session_attributes['repeat_speech_output'] = speech_output
        session_attributes['repeat_reprompt'] = reprompt
        handler_input.attributes_manager.session_attributes = session_attributes
        
        if supports_apl(handler_input):
            handler_input.response_builder.add_directive(
                RenderDocumentDirective(
                    token = "simpleDisplayTemplate",
                    document = _load_apl_document('simpleDisplayTemplate.json'),
                    datasources = {"message": {"text": speech_output}}
                    )
                )
        return handler_input.response_builder.speak(speech_output).ask(reprompt).response

class OrnamentIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("OrnamentIntent")(handler_input)
        
    def handle(self, handler_input):
        logger.info("In OrnamentIntentHandler")
        session_attributes = handler_input.attributes_manager.session_attributes
        speech_output = "You can cover your valuable items like silver or golden ornaments in home insurance, but your premium and policy amount will change accordingly."
        reprompt = "What else would you like to know?"
        session_attributes['repeat_speech_output'] = speech_output
        session_attributes['repeat_reprompt'] = reprompt
        handler_input.attributes_manager.session_attributes = session_attributes
        if supports_apl(handler_input):
            handler_input.response_builder.add_directive(
                RenderDocumentDirective(
                    token = "simpleDisplayTemplate",
                    document = _load_apl_document('simpleDisplayTemplate.json'),
                    datasources = {"message": {"text": speech_output}}
                    )
                )
        return handler_input.response_builder.speak(speech_output).ask(reprompt).response

class ScheduleLossIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("ScheduleLossIntent")(handler_input)
        
    def handle(self, handler_input):
        logger.info("In ScheduleLossIntentHandler")
        session_attributes = handler_input.attributes_manager.session_attributes
        speech_output = "Schedule of loss is a document submitted to theinsurance company to claim the policy; it gives the information of damaged or lost items like model number, when it was purchased, cost of the item etc."
        reprompt = "What else would you like to know?"
        session_attributes['repeat_speech_output'] = speech_output
        session_attributes['repeat_reprompt'] = reprompt
        handler_input.attributes_manager.session_attributes = session_attributes
        if supports_apl(handler_input):
            handler_input.response_builder.add_directive(
                RenderDocumentDirective(
                    token = "simpleDisplayTemplate",
                    document = _load_apl_document('simpleDisplayTemplate.json'),
                    datasources = {"message": {"text": speech_output}}
                    )
                )
        return handler_input.response_builder.speak(speech_output).ask(reprompt).response

class PerilsIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("PerilsIntent")(handler_input)
        
    def handle(self, handler_input):
        logger.info("In PerilsIntentHandler")
        session_attributes = handler_input.attributes_manager.session_attributes
        speech_output = "In home insurance coverage, ‘All perils’ protects you from the widest range of risks besides common risks while ‘Specified perils’ will give coverage only for the common risks, that is listed in your policy."
        reprompt = "What else would you like to know?"
        session_attributes['repeat_speech_output'] = speech_output
        session_attributes['repeat_reprompt'] = reprompt
        handler_input.attributes_manager.session_attributes = session_attributes
        if supports_apl(handler_input):
            handler_input.response_builder.add_directive(
                RenderDocumentDirective(
                    token = "simpleDisplayTemplate",
                    document = _load_apl_document('simpleDisplayTemplate.json'),
                    datasources = {"message": {"text": speech_output}}
                    )
                )
        return handler_input.response_builder.speak(speech_output).ask(reprompt).response

class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)
        
    def handle(self, handler_input):
        logger.info("In HelpIntentHandler")
        speech_output = "This is the help intent."
        return handler_input.response_builder.speak(speech_output).ask(speech_output).response

class CancelOrStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (
            is_intent_name("AMAZON.CancelIntent")(handler_input) or
            is_intent_name("AMAZON.StopIntent")(handler_input)
            )
        
    def handle(self, handler_input):
        logger.info("In CancelOrStopIntentHandler")
        speech_output = "Goodbye."
        return handler_input.response_builder.speak(speech_output).set_should_end_session(True).response

class FallbackIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)
        
    def handle(self, handler_input):
        logger.info("In FallbackIntentHandler")
        speech_output = "This is the fallback intent."
        return handler_input.response_builder.speak(speech_output).ask(speech_output).response

class RepeatIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.RepeatIntent")(handler_input)
        
    def handle(self, handler_input):
        logger.info("In RepeatIntentHandler")
        session_attributes = handler_input.attributes_manager.session_attributes
        speech_output = session_attributes['repeat_speech_output']
        reprompt = session_attributes['repeat_reprompt']
        return handler_input.response_builder.speak(speech_output).ask(speech_output).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("SessionEndedRequest")(handler_input)
        
    def handle(self, handler_input):
        logger.info("In SessionEndedRequestHandler")
        return handler_input.response_builder.response

class CatchAllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True
        
    def handle(self, handler_input, exception):
        logger.error(exception, exc_info = True)
        speech_output = "Sorry, I had trouble doing what you asked. Please try again."
        return handler_input.response_builder.speak(speech_output).ask(speech_output).response

class RequestLogger(AbstractRequestInterceptor):
    def process(self, handler_input):
        #logger.debug("Alexa Request: {}".format(handler_input.request_envelope.request))
        pass

class ResponseLogger(AbstractResponseInterceptor):
    def process(self, handler_input, response):
        #logger.debug("Alexa Response: {}".format(response))
        pass

sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(RepeatIntentHandler())
sb.add_request_handler(OrnamentIntentHandler())
sb.add_request_handler(ScheduleLossIntentHandler())
sb.add_request_handler(PerilsIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

sb.add_global_request_interceptor(RequestLogger())
sb.add_global_response_interceptor(ResponseLogger())

lambda_handler = sb.lambda_handler()