# coding: utf-8
# Copyright (c) 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

##########################################################################
# main.py
# Supports Python 3
##########################################################################
# Info:
# Get texts from LLM model for given prompts using OCI Generative AI Service.
##########################################################################
# Application Command line(no parameter needed)
# python main.py
##########################################################################
#import oci
import prompt_loader

def main():
    # Setup basic variables
    # Auth Config
    # TODO: Please update config profile name and use the compartmentId that has policies grant permissions for using Generative AI Service
    #compartment_id = "ocid1.compartment.oc1..aaaaaaaan7mtnonbklrorqxgiud2evksx6dbnffr2ynkkaa7e3moesbknvsa"
    #CONFIG_PROFILE = "DEFAULT"
    #config = oci.config.from_file('~/.oci/config', CONFIG_PROFILE)
    
    # Service endpoint
    #endpoint = "https://inference.generativeai.eu-frankfurt-1.oci.oraclecloud.com"

    # Load all the SLA documents into memory and fabricate propmts for the LLM chat session
    # TODO: Please add your code here
    prompt = prompt_loader.custom_prompt()
    init_prompt = prompt._initial_dispute_prompt()
    #print(input)



    
    #generative_ai_inference_client = oci.generative_ai_inference.GenerativeAiInferenceClient(config=config, service_endpoint=endpoint, retry_strategy=oci.retry.NoneRetryStrategy(), timeout=(10,240))
    #chat_detail = oci.generative_ai_inference.models.ChatDetails()
    
    #content = oci.generative_ai_inference.models.TextContent()
    #content.text = "{input}"
    #message = oci.generative_ai_inference.models.Message()
    #message.role = "USER"
    #message.content = [content]
    #chat_request = oci.generative_ai_inference.models.GenericChatRequest()
    #chat_request.api_format = oci.generative_ai_inference.models.BaseChatRequest.API_FORMAT_GENERIC
    #chat_request.messages = [message]

    #----------------------------------
    # chat session hyper parameters
    #----------------------------------
    #chat_request.max_tokens = 600
    #chat_request.temperature = 0.9
    #chat_request.frequency_penalty = 0
    #chat_request.presence_penalty = 0
    #chat_request.top_p = 0.7
    #chat_request.top_k = -1

    #chat_detail.serving_mode = oci.generative_ai_inference.models.OnDemandServingMode(model_id="ocid1.generativeaimodel.oc1.eu-frankfurt-1.amaaaaaask7dceyatobkuq6yg3lqeqhawaj3i7pckwaoeyf2liwnzvgtp6ba")
    #chat_detail.chat_request = chat_request
    #chat_detail.compartment_id = compartment_id
    #chat_response = generative_ai_inference_client.chat(chat_detail)
    # Print result
    #print("**************************Chat Result**************************")
    #print(vars(chat_response))

"This is the main class file"
if __name__ == "__main__":
    main()