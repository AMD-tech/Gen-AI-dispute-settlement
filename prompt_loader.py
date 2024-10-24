#############################################################################
# prompt_loader.py
# Supports Python 3
#############################################################################
# Info:
# Read all the SLA documents from the repo and fabricate prompts for the LLM.
#############################################################################

from llama_index.core import PromptTemplate
#from llama_index.llms.openai import OpenAI
import os
import tmpl_lib.dispute_config as disp_conf
import tmpl_lib.dispute_tmpl as disp_tmpl



class custom_prompt:

    doc_list = []   # list that holds the docs from the repo


    def __init__(self):
        os.chdir(".\\repo")
        flist = os.listdir()

        for item in flist:
            file = open(".\\"+item, "r")
            self.doc_list.append(file.read()) # populating the doc_list with the file content
            file.close()
        
        



    # prepare the prompt using the tmpl_lib configuration files and return formatted prompt
    def _initial_dispute_prompt(self):

        prompt_tmpl = PromptTemplate(disp_tmpl.template, template_var_mappings=disp_tmpl.template_var_mappings)
        fmt_prompt = prompt_tmpl.format(
            context_str = disp_conf.config['context_str'],
            pre_task_example_instruction = disp_conf.config['pre_task_example_instruction'],
            task_examples = disp_conf.config['task_examples'],
            post_task_example_instructions = disp_conf.config['post_task_example_instructions'],
            qa_instructions = disp_conf.config['qa_instructions'],
            chat_rules = disp_conf.config['chat_rules']

        )
        return fmt_prompt
        
