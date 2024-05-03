from openai import OpenAI
client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)
chat_completion = client.chat.completions.create(
    messages=[
        {'role': 'assistant','content':'You are a math professor with more than 30 years of experience in trigonomerty.'},
        {'role':'user','content': 'Can you tell me the basic idea behind Pythagoras theorem'},
        {'role':'assistant','content':"One of my favorite topics!\n\nThe fundamental idea behind Pythagoras' theorem is that for a right-angled triangle (where one angle is 90 degrees), the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.\n\nIn mathematical notation, this can be expressed as:\n\na^2 + b^2 = c^2\n\nwhere a and b are the lengths of the two sides that meet at the right angle (called legs), and c is the length of the hypotenuse. This equation holds true regardless of the sizes of the three sides.\n\nPythagoras' theorem has numerous applications in various fields, such as geometry, algebra, physics, engineering, and computer science. It's a fundamental tool for solving problems involving right triangles and is widely used in many areas of mathematics and science"},
        {'role':'user','content': 'Can you explain it in more simple terms please?'},
    ],
    model='llama3',
)
print(chat_completion.choices[0].message.content)
print('---------------------------------')
print('Created at: ',chat_completion.created)
print('Model: ',chat_completion.model)
print('Object: ',chat_completion.object)
print('Finger print: ',chat_completion.system_fingerprint)
print('Completion tokens',chat_completion.usage.completion_tokens)
print('Prompt tokens: ',chat_completion.usage.prompt_tokens)
print('Total tokens: ',chat_completion.usage.total_tokens)