import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

DATA_FILE = "data/user_behavior.csv"

df = pd.read_csv(DATA_FILE)

features = df[[
    "typing_speed",
    "app_count",
    "session_duration"
]]

scaler = StandardScaler()

X = scaler.fit_transform(features)

input_dim = X.shape[1]

input_layer = Input(shape=(input_dim,))

encoder = Dense(8, activation="relu")(input_layer)
encoder = Dense(4, activation="relu")(encoder)

decoder = Dense(8, activation="relu")(encoder)
decoder = Dense(input_dim, activation="linear")(decoder)

autoencoder = Model(inputs=input_layer, outputs=decoder)

autoencoder.compile(
    optimizer="adam",
    loss="mse"
)

autoencoder.fit(
    X,
    X,
    epochs=30,
    batch_size=16,
    shuffle=True
)

autoencoder.save("autoencoder_model.h5")

print("Autoencoder trained successfully")