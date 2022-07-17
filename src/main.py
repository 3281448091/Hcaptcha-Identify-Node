import base64
import json
import random
import time

import requests

from src.solutions import resnet, sk_recognition, yolo

translated_labels_en = {
    "airplane": "airplane",
    "аirplane": "airplane",
    "motorbus": "bus",
    "mοtorbus": "bus",
    "bus": "bus",
    "truck": "truck",
    "truсk": "truck",
    "motorcycle": "motorcycle",
    "mοtorcycle": "motorcycle",
    "boat": "boat",
    "bicycle": "bicycle",
    "bіcycle": "bicycle",
    "train": "train",
    "trаin": "train",
    "vertical river": "vertical river",
    "airplane in the sky flying left": "airplane in the sky flying left",
    "Please select all airplanes in the sky that are flying to the rіght": "airplanes in the sky that are flying to the right",
    "Please select all airplanes in the sky that are flying to the right": "airplanes in the sky that are flying to the right",
    "Please select all the elephants drawn with lеaves": "elephants drawn with leaves",
    "Please select all the elephants drawn with leaves": "elephants drawn with leaves",
    "seaplane": "seaplane",
    "ѕeaplane": "seaplane",
    "car": "car",
    "domestic cat": "domestic cat",
    "domestic сat": "domestic cat",
    "bedroom": "bedroom",
    "bеdroom": "bedroom",
    "lion": "lion",
    "lіon": "lion",
    "brіdge": "bridge",
    "bridge": "bridge",
}


def switch_solution(dir_model, onnx_prefix, label):
    """
    :param dir_model: the directory of the model
    :param onnx_prefix: the name of the onnx file
    :param label: the label of the captcha
    """
    if label in ["seaplane"]:
        return resnet.ResNetSeaplane(dir_model)
    if label in ["elephants drawn with leaves"]:
        return resnet.ElephantsDrawnWithLeaves(dir_model, path_rainbow="src/models/rainbow.yaml")
    if label in ["vertical river"]:
        return sk_recognition.VerticalRiverRecognition(path_rainbow="src/models/rainbow.yaml")
    if label in ["airplane in the sky flying left"]:
        return sk_recognition.LeftPlaneRecognition(path_rainbow="src/models/rainbow.yaml")
    if label in ["airplanes in the sky that are flying to the right"]:
        return sk_recognition.RightPlaneRecognition(path_rainbow="src/models/rainbow.yaml")
    if label in ["horses drawn with flowers"]:
        return resnet.HorsesDrawnWithFlowers(dir_model, path_rainbow="src/models/rainbow.yaml")
    if label in ["lion"]:
        return resnet.ResNetLion(dir_model, path_rainbow="src/models/rainbow.yaml")
    if label in ["bridge"]:
        return resnet.ResNetBridge(dir_model, path_rainbow="src/models/rainbow.yaml")
    if label in ["domestic cat"]:
        return resnet.ResNetDomesticCat(dir_model, path_rainbow="src/models/rainbow.yaml")
    if label in ["bedroom"]:
        return resnet.ResNetBedroom(dir_model, path_rainbow="src/models/rainbow.yaml")
    return yolo.YOLOWithAugmentation(label, dir_model, onnx_prefix, path_rainbow="src/models/rainbow.yaml")


def identifyOne(picture_stream, label):
    model = switch_solution("src/models", "yolov6n", label)
    t0 = time.time()
    result = model.solution(img_stream=picture_stream,
                            label=translated_labels_en[label])
    how_long = time.time() - t0
    # print(result, how_long)
    return True if result else False


def solve(label,url):
    """
    :param url: the url of the image encoded in base64
    :param label: the label of the captcha encoded in base64
    """

    label = base64.b64decode(label).decode("utf-8")
    url = base64.b64decode(url).decode("utf-8")
    print(url)

    img_name = label + str(random.randint(100, 999)) + ".png"
    print(requests.get(url, headers={}).status_code)
    open("static/" + img_name, "wb").write(requests.get(url, headers={}).content)

    img_stream = open("static/" + img_name, "rb").read()
    print(img_stream)


    return identifyOne(img_stream, label)



