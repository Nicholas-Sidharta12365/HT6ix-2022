# import cohere
# from cohere.classify import Example

# co = cohere.Client("BIt19ULiuzKZGybC7rkrP9Si8kEtmuF3SHjyIohZ")

# def generate():
#   classifications = co.classify(
#     model='medium',
#     taskDescription='',
#     outputIndicator='',
#     inputs=["this game sucks,\n  you suck", "you f*g*t", "put your neck in a\n  noose", "buy the black\n  potion", "top mia", "gg well played"],
#     examples=[Example("yo how are you", "benign"), Example("PUDGE MID!", "benign"), Example("I WILL REMEMBER THIS FOREVER", "benign"), Example("I think I saw it first", "benign"), Example("bring me a potion", "benign"), Example("I will honestly kill you", "toxic"), Example("get rekt moron", "toxic"), Example("go to hell", "toxic"), Example("f*a*g*o*t", "toxic"), Example("you are hot trash", "toxic")])
#   return 'The confidence levels of the labels are: {}'.format(classifications.classifications)

import cohere
from cohere.classify import Example
co = cohere.Client("BIt19ULiuzKZGybC7rkrP9Si8kEtmuF3SHjyIohZ")

def generate(text_list):
  response = co.classify(
    model='596c51ba-f4d1-4669-b3c9-51f261bb5ac2-ft',
    inputs=text_list
    )

  response_collection=[]
  for i in response.classifications:
    response_collection.append(i.prediction)
  
  return response_collection

def classify(text): 
  response = co.classify(
    model='596c51ba-f4d1-4669-b3c9-51f261bb5ac2-ft',
    inputs=[text]
    )
  
  confidences = response.classifications[0].confidence
  confidences = [c.confidence for c in confidences]
  return confidences
