# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import pandas as pd
import glob
import fileinput


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:
    (documentación omitida)
    """

    test_negative = []
    files = glob.glob("files/input/test/negative/*")
    with fileinput.input(files=files) as f:
        for line in f:
            test_negative.append(line.strip())

    test_neutral = []
    files = glob.glob("files/input/test/neutral/*")
    with fileinput.input(files=files) as f:
        for line in f:
            test_neutral.append(line.strip())

    test_positive = []
    files = glob.glob("files/input/test/positive/*")
    with fileinput.input(files=files) as f:
        for line in f:
            test_positive.append(line.strip())

    train_negative = []
    files = glob.glob("files/input/train/negative/*")
    with fileinput.input(files=files) as f:
        for line in f:
            train_negative.append(line.strip())

    train_neutral = []
    files = glob.glob("files/input/train/neutral/*")
    with fileinput.input(files=files) as f:
        for line in f:
            train_neutral.append(line.strip())

    train_positive = []
    files = glob.glob("files/input/train/positive/*")
    with fileinput.input(files=files) as f:
        for line in f:
            train_positive.append(line.strip())

    dic_test_negative = [{"phrase": line, "target": "negative"} for line in test_negative]
    dic_test_neutral = [{"phrase": line, "target": "neutral"} for line in test_neutral]
    dic_test_positive = [{"phrase": line, "target": "positive"} for line in test_positive]
    dic_train_negative = [{"phrase": line, "target": "negative"} for line in train_negative]
    dic_train_neutral = [{"phrase": line, "target": "neutral"} for line in train_neutral]
    dic_train_positive = [{"phrase": line, "target": "positive"} for line in train_positive]

    test_dataset = pd.DataFrame(dic_test_positive + dic_test_neutral + dic_test_negative, columns=["phrase", "target"])
    train_dataset = pd.DataFrame(dic_train_positive + dic_train_neutral + dic_train_negative, columns=["phrase", "target"])

    output_folder = "files/output"
    if os.path.exists(output_folder):
        for file in glob.glob(f"{output_folder}/*"):
            os.remove(file)
        os.rmdir(output_folder)
    os.makedirs(output_folder)

    test_path = os.path.join(output_folder, "test_dataset.csv")
    train_path = os.path.join(output_folder, "train_dataset.csv")

    test_dataset.to_csv(test_path, index=False)
    train_dataset.to_csv(train_path, index=False)