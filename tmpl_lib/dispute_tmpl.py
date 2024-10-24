template = """
Context information is below.
---------------------
    {context_str}
---------------------
Given the context information and not prior knowledge,
    {pre_task_example_instruction}
    {task_examples}
    {post_task_example_instructions}
    {qa_instructions}
    {chat_rules}
    """

template_var_mappings = {
        "context_str": "context_str", 
        "pre_task_example_instruction": "pre_task_example_instruction",
        "task_examples": "task_examples",
        "post_task_example_instructions": "post_task_example_instructions",
        "qa_instructions": "qa_instructions",
        "chat_rules": "chat_rules"
         }
