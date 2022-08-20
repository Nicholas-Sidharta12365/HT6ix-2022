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
  classifications = co.classify(
    model='medium',
    taskDescription='',
    outputIndicator='',
    inputs=text_list,
    examples=[Example("yo how are you", "benign"), Example("PUDGE MID!", "benign"), Example("I WILL REMEMBER THIS FOREVER", "benign"), Example("I think I saw it first", "benign"), Example("bring me a potion", "benign"), Example("I will honestly kill you", "toxic"), Example("get rekt moron", "toxic"), Example("go to hell", "toxic"), Example("f*a*g*o*t", "toxic"), Example("you are hot trash", "toxic")])
  return(classifications.classifications[0].prediction)