import pandas as pd
import numpy as np
from statsmodels.tsa.api import SimpleExpSmoothing
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Qt5Agg')

MOOD = ['sad', 'angry', 'curious', 'disgusted', 'fearful', 'happy', 'neutral', 'surprised']

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def normalize(x):
    x = np.array(x)
    return x / x.sum()

def predict_mood(classifications):
    data = np.array([arr.tolist() for arr in classifications])
    result = []
    for i in range(len(MOOD)):
        smoothing = SimpleExpSmoothing(data[:,i] if data.shape[0] != 1 else np.array([data[:, i], data[:, i]])).fit(smoothing_level=0.2, optimized=False)
        fcast = smoothing.forecast(1)
        # print(fcast)
        result.append(fcast[0])
        
    df = pd.DataFrame(data)
    # ax = df.plot(marker='o', color='black', figsize=(12,8), legend=True)
    # smoothing_1.fittedvalues.plot(marker="+", ax=ax, color="blue")

    classify_result = softmax(result)
    # plt.show()
    # print(df)
    # print(normalize(result))
    return (normalize(result), MOOD[np.argmax(classify_result)])

# def retrieve_mood_data(author_id, )