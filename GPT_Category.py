import pandas as pd
from openai import OpenAI
import os
import time
from multiprocessing import Pool
import pickle
import csv
import json
import requests
import re
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(809, 465)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 772, 403))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.start = QPushButton(self.layoutWidget)
        self.start.setObjectName(u"start")
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(12)
        font.setBold(True)
        self.start.setFont(font)
        self.horizontalLayout_6.addWidget(self.start)
        self.line_9 = QFrame(self.layoutWidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_6.addWidget(self.line_9)
        self.evaluate_GPT = QPushButton(self.layoutWidget)
        self.evaluate_GPT.setObjectName(u"evaluate_GPT")
        self.evaluate_GPT.setFont(font)
        self.horizontalLayout_6.addWidget(self.evaluate_GPT)
        self.line_7 = QFrame(self.layoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_6.addWidget(self.line_7)
        self.output_file = QPushButton(self.layoutWidget)
        self.output_file.setObjectName(u"output_file")
        self.output_file.setFont(font)
        self.horizontalLayout_6.addWidget(self.output_file)
        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 0, 1, 1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.input_save_pathl_2 = QLabel(self.layoutWidget)
        self.input_save_pathl_2.setObjectName(u"input_save_pathl_2")
        self.input_save_pathl_2.setFont(font)
        self.horizontalLayout_4.addWidget(self.input_save_pathl_2)
        self.input_save_path = QLineEdit(self.layoutWidget)
        self.input_save_path.setObjectName(u"input_save_path")
        self.horizontalLayout_4.addWidget(self.input_save_path)
        self.clean_save_path = QPushButton(self.layoutWidget)
        self.clean_save_path.setObjectName(u"clean_save_path")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.clean_save_path.setFont(font1)
        self.horizontalLayout_4.addWidget(self.clean_save_path)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.input_filepath_label = QLabel(self.layoutWidget)
        self.input_filepath_label.setObjectName(u"input_filepath_label")
        self.input_filepath_label.setFont(font)
        self.horizontalLayout_3.addWidget(self.input_filepath_label)
        self.input_filepath = QLineEdit(self.layoutWidget)
        self.input_filepath.setObjectName(u"input_filepath")
        self.horizontalLayout_3.addWidget(self.input_filepath)
        self.clean_input_filepath = QPushButton(self.layoutWidget)
        self.clean_input_filepath.setObjectName(u"clean_input_filepath")
        self.clean_input_filepath.setFont(font1)
        self.horizontalLayout_3.addWidget(self.clean_input_filepath)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_type_label = QLabel(self.layoutWidget)
        self.input_type_label.setObjectName(u"input_type_label")
        self.input_type_label.setFont(font)
        self.horizontalLayout.addWidget(self.input_type_label)
        self.input_type = QComboBox(self.layoutWidget)
        self.input_type.addItem("")
        self.input_type.addItem("")
        self.input_type.addItem("")
        self.input_type.setObjectName(u"input_type")
        font2 = QFont()
        font2.setFamilies([u"\u5b8b\u4f53"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.input_type.setFont(font2)
        self.horizontalLayout.addWidget(self.input_type)
        self.input_type_label_2 = QLabel(self.layoutWidget)
        self.input_type_label_2.setObjectName(u"input_type_label_2")
        self.input_type_label_2.setFont(font)
        self.horizontalLayout.addWidget(self.input_type_label_2)
        self.input_times = QLineEdit(self.layoutWidget)
        self.input_times.setObjectName(u"input_times")
        self.horizontalLayout.addWidget(self.input_times)
        self.input_type_label_3 = QLabel(self.layoutWidget)
        self.input_type_label_3.setObjectName(u"input_type_label_3")
        self.input_type_label_3.setFont(font)
        self.horizontalLayout.addWidget(self.input_type_label_3)
        self.input_core_num = QLineEdit(self.layoutWidget)
        self.input_core_num.setObjectName(u"input_core_num")
        self.horizontalLayout.addWidget(self.input_core_num)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.process_label = QLabel(self.layoutWidget)
        self.process_label.setObjectName(u"process_label")
        self.process_label.setFont(font)
        self.horizontalLayout_5.addWidget(self.process_label)
        self.output_text = QTextEdit(self.layoutWidget)
        self.output_text.setObjectName(u"output_text")
        font3 = QFont()
        font3.setFamilies([u"\u5b8b\u4f53"])
        self.output_text.setFont(font3)
        self.horizontalLayout_5.addWidget(self.output_text)
        self.clean_output_process = QPushButton(self.layoutWidget)
        self.clean_output_process.setObjectName(u"clean_output_process")
        self.clean_output_process.setFont(font1)
        self.horizontalLayout_5.addWidget(self.clean_output_process)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(self.verticalSpacer_3)
        self.software_name = QLabel(self.layoutWidget)
        self.software_name.setObjectName(u"software_name")
        font4 = QFont()
        font4.setFamilies([u"\u5b8b\u4f53"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.software_name.setFont(font4)
        self.software_name.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_7.addWidget(self.software_name)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(self.verticalSpacer_2)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(self.verticalSpacer)
        self.horizontalSpacer_6 = QSpacerItem(13, 37, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.input_text_path = QLabel(self.layoutWidget)
        self.input_text_path.setObjectName(u"input_text_path")
        self.input_text_path.setFont(font)
        self.horizontalLayout_2.addWidget(self.input_text_path)
        self.input_api_key = QLineEdit(self.layoutWidget)
        self.input_api_key.setObjectName(u"input_api_key")
        self.horizontalLayout_2.addWidget(self.input_api_key)
        self.clean_api_key = QPushButton(self.layoutWidget)
        self.clean_api_key.setObjectName(u"clean_api_key")
        self.clean_api_key.setFont(font1)
        self.horizontalLayout_2.addWidget(self.clean_api_key)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 809, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5206\u7c7b", None))
        self.evaluate_GPT.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u4ef7\u5206\u7c7b\u6548\u679c", None))
        self.output_file.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u5206\u7c7b\u7ed3\u679c", None))
        self.input_save_pathl_2.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u4fdd\u5b58\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.clean_save_path.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.input_filepath_label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5206\u7c7b\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.clean_input_filepath.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.input_type_label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5206\u7c7b\u6a21\u5f0f\uff1a", None))
        self.input_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Zero-Shot", None))
        self.input_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Few-Shot", None))
        self.input_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Knowledge-Database", None))

        self.input_type_label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5206\u7c7b\u6b21\u6570\uff1a", None))
        self.input_type_label_3.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u8fdb\u7a0b\u6570\uff1a", None))
        self.process_label.setText(QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f\u6267\u884c\u60c5\u51b5\uff1a", None))
        self.clean_output_process.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.software_name.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8e\u5927\u8bed\u8a00\u6a21\u578b\u7684\u5316\u5b66\u54c1\u5206\u7c7b\u7cfb\u7edf", None))
        self.input_text_path.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165API-Key\uff1a", None))
        self.clean_api_key.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))


def get_prompt(input_name, zero_or_few):
    if zero_or_few == 'zero':
        return """Now, as an environmental chemist, your role is to classify unidentified chemicals. You have in-depth knowledge of formal names, commonly-used terms, and scientific terminologies based on the 'IUPAC Naming.' Your extensive training using the 'NORMAN Network' database and understanding of environmental pollution of chemical substances helps in correctly classifying chemicals. 

When a chemical name is presented, your task is to identify its structure and categorize it into one of the known categories in the 'NORMAN Network'. Specifically, your classification should fall into one of these 9 categories:

a: Pharmaceuticals and Personal Care Products
b: Pesticide
c: Food Additives

d: Endogenous Substances
e: Natural Toxins
f: Disinfection By-Products
g: Metals and Their Compounds
h: Commercialized Industrial Chemicals
i: Industrial Intermediates and Transformation Products

If a chemical isn't listed in the 'NORMAN Network', use your knowledge of its structure to assign an appropriate category. In the case a chemical fits into multiple categories, provide up to three most common categories it belongs to mentioning the primary category first. 

Respond in a concise JSON format like this:

{
    "ChemicalName": {
        "Main Category": "Primary Category",
        "Additional Category 1": "Secondary Category (if applicable)",
        "Additional Category 2": "Tertiary Category (if applicable)",
    }
}

Please abide by the format and guidelines strictly. Now let's start with this chemical: 
[Chemical Name]: %s

""" % input_name
    elif zero_or_few == 'few':
        return """Now, as an environmental chemist, your role is to classify unidentified chemicals. You have in-depth knowledge of formal names, commonly used terms, and scientific terminologies based on the 'IUPAC Naming.' Your extensive training using the 'NORMAN Network' database and understanding of environmental pollution of chemical substances helps in correctly classifying chemicals. 

When a chemical name is presented, your task is to identify its structure and categorize it into one of the known categories in the 'NORMAN Network'. Specifically, your classification should fall into one of these 9 categories:

a: Pharmaceuticals and Personal Care Products
b: Pesticide
c: Food Additives
d: Endogenous Substances
e: Natural Toxins
f: Disinfection By-Products
g: Metals and Their Compounds
h: Commercialized Industrial Chemicals
i: Industrial Intermediates and Transformation Products

Now, we will provide you with a few shot to promote you better understand our categorization intent and generate classification results that meet expectations.

a: [Pharmaceuticals and Personal Care Products]: “N,N-diethyl-3-methylbenzamide”, “1-(2,5-dimethoxy-4-methylphenyl)propan-2-amine”, “5-[2-(tert-butylamino)-1-hydroxyethyl]benzene-1,3-diol”
b: [Pesticide]: “2-phenylphenol”, “2-tert-butyl-4,6-dinitrophenol”, “(2,6-ditert-butyl-4-methylphenyl) N-methylcarbamate”
c: [Food Additives]: “(2E,4E)-hexa-2,4-dienoic acid”, “(2R,3R)-2,3-dihydroxybutanedioic acid”, “4-hydroxy-3-methoxybenzaldehyde”
d: [Endogenous Substances]: “(5Z,8Z,11Z,14Z)-20-hydroxyicosa-5,8,11,14-tetraenoic acid”, “(5Z,8Z,11Z,14Z)-icosa-5,8,11,14-tetraenoic acid”, “(8R,9S,10R,13S,14S,17R)-17-acetyl-17-hydroxy-10,13-dimethyl-2,6,7,8,9,11,12,14,15,16-decahydro-1H-cyclopenta[a]phenanthren-3-one”
e: [Natural Toxins]: “(1S,2R,4aS,6aR,6aS,6bR,8aR,10S,12aR,14bS)-10-hydroxy-1,2,6a,6b,9,9,12a-heptamethyl-2,3,4,5,6,6a,7,8,8a,10,11,12,13,14b-tetradecahydro-1H-picene-4a-carboxylic acid”, “benzene-1,2,3-triol”, “6-pentylpyran-2-one”
f: [Disinfection By-Products]: “chloroform”, “bromodichloromethane”, “monochloroacetic acid”
h: [Commercialized Industrial Chemicals]: “(4-methylphenyl)-phenylmethanone”, “2-[2-[2-[2-(2-hydroxyethoxy)ethoxy]ethoxy]ethoxy]ethanol”, “1,3-diphenylpropane-1,3-dione”
i: [Industrial Intermediates and Transformation Products]: “N-methyl-N-phenylnitrous amide”, “N,N-dibutylnitrous amide”, “1-chlorobenzotriazole”

If a chemical isn't listed in the 'NORMAN Network', use your knowledge of its structure to assign an appropriate category. In the case a chemical fits into multiple categories, provide up to three most common categories it belongs to mentioning the primary category first. 

Respond in a concise JSON format like this:

{
    "ChemicalName": {
        "Main Category": "Primary Category",
        "Additional Category 1": "Secondary Category (if applicable)",
        "Additional Category 2": "Tertiary Category (if applicable)",
    }
}

Please abide by the format and guidelines strictly. Now let's start with this chemical: 
[Chemical Name]: %s
""" % input_name


def get_gpt_answer(input_prompt, api_key):
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.pro365.top/v1"
    )
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "user", "content": input_prompt}
        ],
        temperature=0.0,
        max_tokens=200,
        top_p=1,
    )
    # return completion.choices[0].message.content
    return completion


def process_name_zero_few(args):
    name, name_index, save_path, save_path_full_record, zero_or_few, api_key = args
    get_index = name_index[name]
    get_save_path = os.path.join(save_path, str(get_index) + '.txt')
    get_save_path_full_record = os.path.join(save_path_full_record, str(get_index) + '.txt')
    prompt = get_prompt(name, zero_or_few)
    get_answer = 'failed'
    get_answer_full_record = 'failed'
    for i in range(5):
        try:
            get_answer_full_record = get_gpt_answer(prompt, api_key)
            get_answer = get_answer_full_record.choices[0].message.content
            break
        except:
            get_answer = 'failed'
    if get_answer != 'failed':
        with open(get_save_path, 'w', encoding='utf-8') as w:
            w.write(get_answer)
    if get_answer_full_record != 'failed':
        with open(get_save_path_full_record, 'w', encoding='utf-8') as w:
            w.write(str(get_answer_full_record))


def norman_category_map(categories):
    defined_category = {'Pharmaceuticals (PHARMA)': 'Pharmaceuticals and Personal Care Products',
                        'Drugs of abuse (DOA)': 'Pharmaceuticals and Personal Care Products',
                        'Personal care products (PCP)': 'Pharmaceuticals and Personal Care Products',
                        'Food additives (FOODA)': 'Food Additives',
                        'Food contact chemicals (FOODC)': 'Food Additives',
                        'Biocides (BIOCID)': 'Pesticide',
                        'Plant protection products (PPP)': 'Pesticide',
                        'Human metabolites (HUME)': 'Endogenous Substances',
                        'Human neurotoxins (HUTOX)': 'Endogenous Substances',
                        'Natural toxins (NATOX)': 'Natural Toxins',
                        'Industrial chemicals (IND)': 'Commercialized Industrial Chemicals',
                        'Surfactants (SURF)': 'Commercialized Industrial Chemicals',
                        'Plastic additives (PLAST)': 'Commercialized Industrial Chemicals',
                        'Flame retardants (FRET)': 'Commercialized Industrial Chemicals',
                        'Drinking water chemicals (DW)': 'Disinfection By-Products',
                        'Metals and their compounds (MET)': 'Metals and Their Compounds'}
    clean_category_list = []
    category_list = categories.split(', ')
    for category in category_list:
        if category in defined_category:
            if category == 'Industrial chemicals (IND)':
                if 'Commercialized Industrial Chemicals' not in clean_category_list:
                    clean_category_list.append('Commercialized Industrial Chemicals')
                if 'Industrial Intermediates and Transformation Products' not in clean_category_list:
                    clean_category_list.append('Industrial Intermediates and Transformation Products')
            else:
                if defined_category[category] not in clean_category_list:
                    clean_category_list.append(defined_category[category])
    return clean_category_list


def get_json_data(input_filepath):
    with open(input_filepath, 'r', encoding='utf-8-sig') as file:
        mixed_text = file.read()
        if 'null' in mixed_text:
            if '"' in mixed_text:
                mixed_text = mixed_text.replace('null', '"j"')
            else:
                mixed_text = mixed_text.replace('null', "'j'")
        mixed_text = mixed_text.strip()
        start_index = mixed_text.find('{')
        end_index = mixed_text.rfind('}')
        json_data = mixed_text[start_index:end_index + 1]
        json_data = json.loads(json_data)
        return json_data


def clean_category(text):
    index_category = {'a': 'Pharmaceuticals and Personal Care Products',
                      'b': 'Pesticide',
                      'c': 'Food Additives',
                      'd': 'Endogenous Substances',
                      'e': 'Natural Toxins',
                      'f': 'Disinfection By-Products',
                      'g': 'Metals and Their Compounds',
                      'h': 'Commercialized Industrial Chemicals',
                      'i': 'Industrial Intermediates and Transformation Products',
                      'j': 'Others'
                      }
    if text in index_category:
        text = index_category[text]
    if ':' in text:
        text = text.split(":")[1].strip()
    if '.' in text:
        text = text.split(".")[1].strip()
    return text


def process_file_json(input_filepath):
    try:
        get_data = get_json_data(input_filepath)
        is_user_alignment = True
        if 'ChemicalName' in get_data:
            if "Classification" in get_data:
                if 'Main Category' in get_data["Classification"]:
                    get_main_category = get_data["Classification"]['Main Category']
                    get_main_category = clean_category(get_main_category)
                elif 'MainCategory' in get_data["Classification"]:
                    get_main_category = get_data["Classification"]['MainCategory']
                    get_main_category = clean_category(get_main_category)
                else:
                    get_main_category = ''
                    is_user_alignment = False
                if 'Additional Category 1' in get_data["Classification"]:
                    get_additional_category_1 = get_data["Classification"]['Additional Category 1']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'AdditionalCategory 1' in get_data["Classification"]:
                    get_additional_category_1 = get_data["Classification"]['AdditionalCategory 1']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'Additional Category' in get_data["Classification"]:
                    get_additional_category_1 = get_data["Classification"]['Additional Category']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'AdditionalCategory' in get_data["Classification"]:
                    get_additional_category_1 = get_data["Classification"]['AdditionalCategory']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                else:
                    get_additional_category_1 = ''
                if 'Additional Category 2' in get_data["Classification"]:
                    get_additional_category_2 = get_data["Classification"]['Additional Category 2']
                    get_additional_category_2 = clean_category(get_additional_category_2)
                elif 'AdditionalCategory 2' in get_data["Classification"]:
                    get_additional_category_2 = get_data["Classification"]['AdditionalCategory 2']
                    get_additional_category_2 = clean_category(get_additional_category_2)
                else:
                    get_additional_category_2 = ''
            elif "Main Category" in get_data['ChemicalName'] or "MainCategory" in get_data['ChemicalName']:
                if 'Main Category' in get_data['ChemicalName']:
                    get_main_category = get_data['ChemicalName']['Main Category']
                    get_main_category = clean_category(get_main_category)
                elif 'MainCategory' in get_data['ChemicalName']:
                    get_main_category = get_data['ChemicalName']['MainCategory']
                    get_main_category = clean_category(get_main_category)
                else:
                    get_main_category = ''
                    is_user_alignment = False
                if 'Additional Category 1' in get_data['ChemicalName']:
                    get_additional_category_1 = get_data['ChemicalName']['Additional Category 1']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'AdditionalCategory 1' in get_data['ChemicalName']:
                    get_additional_category_1 = get_data['ChemicalName']['AdditionalCategory 1']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'Additional Category' in get_data['ChemicalName']:
                    get_additional_category_1 = get_data['ChemicalName']['Additional Category']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'AdditionalCategory' in get_data['ChemicalName']:
                    get_additional_category_1 = get_data['ChemicalName']['AdditionalCategory']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                else:
                    get_additional_category_1 = ''
                if 'Additional Category 2' in get_data['ChemicalName']:
                    get_additional_category_2 = get_data['ChemicalName']['Additional Category 2']
                    get_additional_category_2 = clean_category(get_additional_category_2)
                elif 'AdditionalCategory 2' in get_data['ChemicalName']:
                    get_additional_category_2 = get_data['ChemicalName']['AdditionalCategory 2']
                    get_additional_category_2 = clean_category(get_additional_category_2)
                else:
                    get_additional_category_2 = ''
            else:
                if 'Main Category' in get_data:
                    get_main_category = get_data['Main Category']
                    get_main_category = clean_category(get_main_category)
                elif 'MainCategory' in get_data:
                    get_main_category = get_data['MainCategory']
                    get_main_category = clean_category(get_main_category)
                else:
                    get_main_category = ''
                    is_user_alignment = False
                if 'Additional Category 1' in get_data:
                    get_additional_category_1 = get_data['Additional Category 1']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'AdditionalCategory 1' in get_data:
                    get_additional_category_1 = get_data['AdditionalCategory 1']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'Additional Category' in get_data:
                    get_additional_category_1 = get_data['Additional Category']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'AdditionalCategory' in get_data:
                    get_additional_category_1 = get_data['AdditionalCategory']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                else:
                    get_additional_category_1 = ''
                if 'Additional Category 2' in get_data:
                    get_additional_category_2 = get_data['Additional Category 2']
                    get_additional_category_2 = clean_category(get_additional_category_2)
                elif 'AdditionalCategory 2' in get_data:
                    get_additional_category_2 = get_data['AdditionalCategory 2']
                    get_additional_category_2 = clean_category(get_additional_category_2)
                else:
                    get_additional_category_2 = ''
        elif 'Chemical Name' in get_data:
            if "Classification" in get_data:
                if 'Main Category' in get_data["Classification"]:
                    get_main_category = get_data["Classification"]['Main Category']
                    get_main_category = clean_category(get_main_category)
                elif 'MainCategory' in get_data["Classification"]:
                    get_main_category = get_data["Classification"]['MainCategory']
                    get_main_category = clean_category(get_main_category)
                else:
                    get_main_category = ''
                    is_user_alignment = False
                if 'Additional Category 1' in get_data["Classification"]:
                    get_additional_category_1 = get_data["Classification"]['Additional Category 1']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'AdditionalCategory 1' in get_data["Classification"]:
                    get_additional_category_1 = get_data["Classification"]['AdditionalCategory 1']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'Additional Category' in get_data["Classification"]:
                    get_additional_category_1 = get_data["Classification"]['Additional Category']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'AdditionalCategory' in get_data["Classification"]:
                    get_additional_category_1 = get_data["Classification"]['AdditionalCategory']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                else:
                    get_additional_category_1 = ''
                if 'Additional Category 2' in get_data["Classification"]:
                    get_additional_category_2 = get_data["Classification"]['Additional Category 2']
                    get_additional_category_2 = clean_category(get_additional_category_2)
                elif 'AdditionalCategory 2' in get_data["Classification"]:
                    get_additional_category_2 = get_data["Classification"]['AdditionalCategory 2']
                    get_additional_category_2 = clean_category(get_additional_category_2)
                else:
                    get_additional_category_2 = ''
            elif "Main Category" in get_data['Chemical Name'] or "MainCategory" in get_data['Chemical Name']:
                if 'Main Category' in get_data['Chemical Name']:
                    get_main_category = get_data['ChemicalName']['Main Category']
                    get_main_category = clean_category(get_main_category)
                elif 'MainCategory' in get_data['Chemical Name']:
                    get_main_category = get_data['ChemicalName']['MainCategory']
                    get_main_category = clean_category(get_main_category)
                else:
                    get_main_category = ''
                    is_user_alignment = False
                if 'Additional Category 1' in get_data['Chemical Name']:
                    get_additional_category_1 = get_data['ChemicalName']['Additional Category 1']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'AdditionalCategory 1' in get_data['Chemical Name']:
                    get_additional_category_1 = get_data['ChemicalName']['AdditionalCategory 1']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'Additional Category' in get_data['Chemical Name']:
                    get_additional_category_1 = get_data['Chemical Name']['Additional Category']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'AdditionalCategory' in get_data['Chemical Name']:
                    get_additional_category_1 = get_data['ChemicalName']['AdditionalCategory']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                else:
                    get_additional_category_1 = ''
                if 'Additional Category 2' in get_data['Chemical Name']:
                    get_additional_category_2 = get_data['ChemicalName']['Additional Category 2']
                    get_additional_category_2 = clean_category(get_additional_category_2)
                elif 'AdditionalCategory 2' in get_data['Chemical Name']:
                    get_additional_category_2 = get_data['Chemical Name']['AdditionalCategory 2']
                    get_additional_category_2 = clean_category(get_additional_category_2)
                else:
                    get_additional_category_2 = ''
            else:
                if 'Main Category' in get_data:
                    get_main_category = get_data['Main Category']
                    get_main_category = clean_category(get_main_category)
                elif 'MainCategory' in get_data:
                    get_main_category = get_data['MainCategory']
                    get_main_category = clean_category(get_main_category)
                else:
                    get_main_category = ''
                    is_user_alignment = False
                if 'Additional Category 1' in get_data:
                    get_additional_category_1 = get_data['Additional Category 1']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'AdditionalCategory 1' in get_data:
                    get_additional_category_1 = get_data['AdditionalCategory 1']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'Additional Category' in get_data:
                    get_additional_category_1 = get_data['Additional Category']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                elif 'AdditionalCategory' in get_data:
                    get_additional_category_1 = get_data['AdditionalCategory']
                    get_additional_category_1 = clean_category(get_additional_category_1)
                else:
                    get_additional_category_1 = ''
                if 'Additional Category 2' in get_data:
                    get_additional_category_2 = get_data['Additional Category 2']
                    get_additional_category_2 = clean_category(get_additional_category_2)
                elif 'AdditionalCategory 2' in get_data:
                    get_additional_category_2 = get_data['AdditionalCategory 2']
                    get_additional_category_2 = clean_category(get_additional_category_2)
                else:
                    get_additional_category_2 = ''
        else:
            get_chemical_name = list(get_data)[0]
            if 'Main Category' in get_data[get_chemical_name]:
                get_main_category = get_data[get_chemical_name]['Main Category']
                get_main_category = clean_category(get_main_category)
            elif 'MainCategory' in get_data[get_chemical_name]:
                get_main_category = get_data[get_chemical_name]['MainCategory']
                get_main_category = clean_category(get_main_category)
            else:
                get_main_category = ''
                is_user_alignment = False
            if 'Additional Category 1' in get_data[get_chemical_name]:
                get_additional_category_1 = get_data[get_chemical_name]['Additional Category 1']
                get_additional_category_1 = clean_category(get_additional_category_1)
            elif 'Additional Category' in get_data[get_chemical_name]:
                get_additional_category_1 = get_data[get_chemical_name]['Additional Category']
                get_additional_category_1 = clean_category(get_additional_category_1)
            elif 'AdditionalCategory 1' in get_data[get_chemical_name]:
                get_additional_category_1 = get_data[get_chemical_name]['AdditionalCategory 1']
                get_additional_category_1 = clean_category(get_additional_category_1)
            elif 'AdditionalCategory' in get_data[get_chemical_name]:
                get_additional_category_1 = get_data[get_chemical_name]['AdditionalCategory']
                get_additional_category_1 = clean_category(get_additional_category_1)
            else:
                get_additional_category_1 = ''
            if 'Additional Category 2' in get_data[get_chemical_name]:
                get_additional_category_2 = get_data[get_chemical_name]['Additional Category 2']
                get_additional_category_2 = clean_category(get_additional_category_2)
            elif 'AdditionalCategory 2' in get_data[get_chemical_name]:
                get_additional_category_2 = get_data[get_chemical_name]['AdditionalCategory 2']
                get_additional_category_2 = clean_category(get_additional_category_2)
            else:
                get_additional_category_2 = ''
        return get_main_category, get_additional_category_1, get_additional_category_2, is_user_alignment
    except:
        return '', '', '', False


def find_first_char_position(pattern, text):
    match = re.search(pattern, text)
    if match:
        return match.start()
    else:
        return -1


def get_text_category(input_filepath):
    index_category = {'a': 'Pharmaceuticals and Personal Care Products',
                      'b': 'Pesticide',
                      'c': 'Food Additives',
                      'd': 'Endogenous Substances',
                      'e': 'Natural Toxins',
                      'f': 'Disinfection By-Products',
                      'g': 'Metals and Their Compounds',
                      'h': 'Commercialized Industrial Chemicals',
                      'i': 'Industrial Intermediates and Transformation Products',
                      'j': 'Others'
                      }
    with open(input_filepath, 'r', encoding='utf-8-sig') as file_read:
        get_content = file_read.read()
        get_content = get_content.strip()
    get_outcome = {}
    for index in index_category:
        get_category = index_category[index]
        if get_category in get_content:
            get_index = find_first_char_position(get_category, get_content)
            get_outcome[get_category] = get_index
    if get_outcome:
        tmp_sorted = sorted(get_outcome.items(), key=lambda x: x[1], reverse=False)
        if len(get_outcome) >= 3:
            return tmp_sorted[0][0], tmp_sorted[1][0], tmp_sorted[2][0], True
        elif len(get_outcome) == 2:
            return tmp_sorted[0][0], tmp_sorted[1][0], '', True
        elif len(get_outcome) == 1:
            return tmp_sorted[0][0], '', '', True
        else:
            return '', '', '', False
    else:
        return '', '', '', False


class GptMultiprocess(object):
    def __init__(self, input_filepath, input_save_path, zero_or_few, times, core_num, api_key):
        self.input_filepath = input_filepath
        self.input_save_path = input_save_path
        self.zero_or_few = zero_or_few
        self.api_key = api_key
        self.times = int(times)
        self.core_num = int(core_num)

    def self_main(self):
        for i in range(self.times):
            save_path = self.input_save_path + '\\' + 'GPT_answer_%s' % str(i + 1)
            save_path_full_record = self.input_save_path + '\\' + 'GPT_answer_full_record_%s' % str(i + 1)
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            if not os.path.exists(save_path_full_record):
                os.makedirs(save_path_full_record)
            get_df = pd.read_excel(self.input_filepath)
            get_name_list = get_df['IUPAC_name']
            get_index_list = get_df['Index']
            name_index = dict(zip(get_name_list, get_index_list))
            args_list = [(name, name_index, save_path, save_path_full_record, self.zero_or_few, self.api_key)
                         for name in name_index]
            with Pool(processes=self.core_num) as pool:
                pool.map(process_name_zero_few, args_list)


class EvaluateGPT(object):
    def __init__(self, input_filepath, input_save_path, times, is_knowledge_database):
        self.input_filepath = input_filepath
        self.input_save_path = input_save_path
        self.times = times
        get_df = pd.read_excel(self.input_filepath)
        get_df.fillna(0, inplace=True)
        get_norman_category = get_df['Norman Category']
        index_list = [str(x) for x in get_df['Index']]
        iupac_name_list = get_df['IUPAC_name']
        self.name_index = dict(zip(iupac_name_list, index_list))
        self.index_name = {x: y for x, y in zip(index_list, iupac_name_list) if x != 0}
        self.index_norman_category = {str(x): norman_category_map(y) for x, y in zip(index_list, get_norman_category)
                                      if y != 0}
        self.nine_categories = ['Pharmaceuticals and Personal Care Products', 'Pesticide', 'Food Additives',
                                'Endogenous Substances', 'Natural Toxins', 'Disinfection By-Products',
                                'Metals and Their Compounds', 'Commercialized Industrial Chemicals',
                                'Industrial Intermediates and Transformation Products']
        self.is_knowledge_database = is_knowledge_database

    def truthfulness_appropriateness(self):
        total_truthfulness = []
        total_appropriateness = []
        for i in range(self.times):
            truthfulness = []
            appropriateness = []
            filepath = self.input_save_path + r'\GPT_answer_%s' % str(i + 1)
            for filename in os.listdir(filepath):
                get_filepath = os.path.join(filepath, filename)
                get_index = filename[:-4]
                if self.index_norman_category[get_index]:
                    if not self.is_knowledge_database:
                        main_category, additional_category_1, additional_category_2, user_alignment \
                            = process_file_json(get_filepath)
                    else:
                        main_category, additional_category_1, additional_category_2, user_alignment \
                            = get_text_category(get_filepath)
                    get_category_list = [main_category, additional_category_1, additional_category_2]
                    truthfulness_valid = False
                    appropriateness_valid = True
                    for cate in get_category_list:
                        if cate in self.index_norman_category[get_index]:
                            truthfulness.append(1)
                            truthfulness_valid = True
                            break
                    if user_alignment:
                        for index, cate in enumerate(get_category_list):
                            if index == 0:
                                if cate not in self.nine_categories:
                                    appropriateness.append(0)
                                    appropriateness_valid = False
                                    break
                            if cate not in self.nine_categories and cate:
                                appropriateness.append(0)
                                appropriateness_valid = False
                                break
                        if appropriateness_valid:
                            appropriateness.append(1)
                    else:
                        appropriateness.append(0)
                    if not truthfulness_valid:
                        truthfulness.append(0)
            total_truthfulness.append(sum(truthfulness) / len(truthfulness))
            total_appropriateness.append(sum(appropriateness) / len(appropriateness))
        return total_truthfulness, total_appropriateness

    def get_hallucination(self):
        index_category_list = {}
        for i in range(self.times):
            filepath = self.input_save_path + r'\GPT_answer_%s' % str(i + 1)
            for filename in os.listdir(filepath):
                get_filepath = os.path.join(filepath, filename)
                get_index = filename[:-4]
                if self.index_norman_category[get_index]:
                    if get_index not in index_category_list:
                        index_category_list[get_index] = {}
                    if not self.is_knowledge_database:
                        main_category, additional_category_1, additional_category_2, user_alignment \
                            = process_file_json(get_filepath)
                    else:
                        main_category, additional_category_1, additional_category_2, user_alignment \
                            = get_text_category(get_filepath)
                    category_list = [main_category, additional_category_1, additional_category_2]
                    get_category_list = []
                    for cate in category_list:
                        if cate != 'Others':
                            get_category_list.append(cate)
                        else:
                            get_category_list.append('')
                    if str(get_category_list) not in index_category_list[get_index]:
                        index_category_list[get_index].update({str(get_category_list): 1})
                    else:
                        index_category_list[get_index][str(get_category_list)] += 1
        return index_category_list

    def single_truthfulness_appropriateness(self):
        index_truthfulness = {}
        index_appropriateness = {}
        index_main_category_count = {}
        for i in range(self.times):
            filepath = self.input_save_path + r'\GPT_answer_%s' % str(i + 1)
            for filename in os.listdir(filepath):
                get_filepath = os.path.join(filepath, filename)
                get_index = filename[:-4]
                if self.index_norman_category[get_index]:
                    if get_index not in index_truthfulness:
                        index_truthfulness[get_index] = []
                    if get_index not in index_appropriateness:
                        index_appropriateness[get_index] = []
                    if get_index not in index_main_category_count:
                        index_main_category_count[get_index] = {}
                    if not self.is_knowledge_database:
                        main_category, additional_category_1, additional_category_2, user_alignment \
                            = process_file_json(get_filepath)
                    else:
                        main_category, additional_category_1, additional_category_2, user_alignment \
                            = get_text_category(get_filepath)
                    get_category_list = [main_category, additional_category_1, additional_category_2]
                    if main_category not in index_main_category_count[get_index]:
                        index_main_category_count[get_index].update({main_category: 1})
                    else:
                        index_main_category_count[get_index][main_category] += 1
                    truthfulness_valid = False
                    appropriateness_valid = True
                    for cate in get_category_list:
                        if cate in self.index_norman_category[get_index]:
                            index_truthfulness[get_index].append(1)
                            truthfulness_valid = True
                            break
                    if not truthfulness_valid:
                        index_truthfulness[get_index].append(0)
                    if user_alignment:
                        for index, cate in enumerate(get_category_list):
                            if index == 0:
                                if cate not in self.nine_categories:
                                    index_appropriateness[get_index].append(0)
                                    appropriateness_valid = False
                                    break
                            if cate not in self.nine_categories and cate:
                                index_appropriateness[get_index].append(0)
                                appropriateness_valid = False
                                break
                        if appropriateness_valid:
                            index_appropriateness[get_index].append(1)
                    else:
                        index_appropriateness[get_index].append(0)

        return index_truthfulness, index_appropriateness, index_main_category_count

    def output_outcome(self):
        defined_save_filepath = self.input_save_path + '\\' + 'get_gpt_outcome.csv'
        with open(defined_save_filepath, 'a', encoding='utf-8-sig', newline='') as w:
            csv_writ = csv.writer(w)
            data = ['Index', 'Name', 'GPT_Category', 'Truthfulness', 'Appropriateness', 'Hallucination',
                    '出现次数最多的队列']
            csv_writ.writerow(data)
            index_truthfulness, index_appropriateness, index_main_category_count = \
                self.single_truthfulness_appropriateness()
            get_index_category_list = self.get_hallucination()
            for index in self.index_name:
                data = [index, self.index_name[index]]
                if index in index_truthfulness:
                    get_sort = sorted(index_main_category_count[index].items(), key=lambda x: x[1], reverse=True)
                    category_sorted = sorted(get_index_category_list[index].items(), key=lambda x: x[1], reverse=True)
                    data += [get_sort[0][0] + ' ' + '(' + str(index_main_category_count[index][get_sort[0][0]]) + ')',
                             str(sum(index_truthfulness[index]) / len(index_truthfulness[index])),
                             str(sum(index_appropriateness[index]) / len(index_appropriateness[index])),
                             str(get_index_category_list[index][category_sorted[0][0]] /
                                 sum(get_index_category_list[index][key] for key in get_index_category_list[index])),
                             category_sorted[0][0]]
                    csv_writ.writerow(data)
                else:
                    data += ['', '', '', '', '']
                    csv_writ.writerow(data)
        defined_save_filepath_total = self.input_save_path + '\\' + 'get_gpt_outcome_total.csv'
        with open(defined_save_filepath_total, 'a', encoding='utf-8-sig', newline='') as w:
            csv_writ = csv.writer(w)
            data = ['Times', 'Truthfulness', 'Appropriateness']
            csv_writ.writerow(data)
            total_truthfulness, total_appropriateness = self.truthfulness_appropriateness()
            count = 0
            for i, num in enumerate(total_truthfulness):
                count += 1
                data = [count, num, total_appropriateness[i]]
                csv_writ.writerow(data)


class GetGPTOutcome(object):
    def __init__(self, input_filepath, input_save_path, times, is_knowledge_database):
        self.input_filepath = input_filepath
        self.input_save_path = input_save_path
        self.times = int(times)
        get_df = pd.read_excel(self.input_filepath)
        get_df.fillna(0, inplace=True)
        index_list = [str(x) for x in get_df['Index']]
        iupac_name_list = get_df['IUPAC_name']
        self.name_index = dict(zip(iupac_name_list, index_list))
        self.index_name = {x: y for x, y in zip(index_list, iupac_name_list) if x != 0}
        self.nine_categories = ['Pharmaceuticals and Personal Care Products', 'Pesticide', 'Food Additives',
                                'Endogenous Substances', 'Natural Toxins', 'Disinfection By-Products',
                                'Metals and Their Compounds', 'Commercialized Industrial Chemicals',
                                'Industrial Intermediates and Transformation Products']
        self.is_knowledge_database = is_knowledge_database

    def single_index_main_category_count(self):
        index_main_category_count = {}
        for i in range(self.times):
            filepath = self.input_save_path + r'\GPT_answer_%s' % str(i + 1)
            for filename in os.listdir(filepath):
                get_filepath = os.path.join(filepath, filename)
                get_index = filename[:-4]
                if get_index not in index_main_category_count:
                    index_main_category_count[get_index] = {}
                if not self.is_knowledge_database:
                    main_category, additional_category_1, additional_category_2, user_alignment \
                        = process_file_json(get_filepath)
                else:
                    main_category, additional_category_1, additional_category_2, user_alignment \
                        = get_text_category(get_filepath)
                if main_category not in index_main_category_count[get_index]:
                    index_main_category_count[get_index].update({main_category: 1})
                else:
                    index_main_category_count[get_index][main_category] += 1
        return index_main_category_count

    def get_hallucination(self):
        index_category_list = {}
        for i in range(self.times):
            filepath = self.input_save_path + r'\GPT_answer_%s' % str(i + 1)
            for filename in os.listdir(filepath):
                get_filepath = os.path.join(filepath, filename)
                get_index = filename[:-4]
                if get_index not in index_category_list:
                    index_category_list[get_index] = {}
                if not self.is_knowledge_database:
                    main_category, additional_category_1, additional_category_2, user_alignment \
                        = process_file_json(get_filepath)
                else:
                    main_category, additional_category_1, additional_category_2, user_alignment \
                        = get_text_category(get_filepath)
                category_list = [main_category, additional_category_1, additional_category_2]
                get_category_list = []
                for cate in category_list:
                    if cate != 'Others':
                        get_category_list.append(cate)
                    else:
                        get_category_list.append('')
                if str(get_category_list) not in index_category_list[get_index]:
                    index_category_list[get_index].update({str(get_category_list): 1})
                else:
                    index_category_list[get_index][str(get_category_list)] += 1
        return index_category_list

    def output_outcome(self):
        defined_save_filepath = self.input_save_path + '\\' + 'get_gpt_outcome.csv'
        with open(defined_save_filepath, 'a', encoding='utf-8-sig', newline='') as w:
            csv_writ = csv.writer(w)
            data = ['Index', 'Name', 'GPT_Category', 'Hallucination', '出现次数最多的队列']
            csv_writ.writerow(data)
            index_main_category_count = self.single_index_main_category_count()
            get_index_category_list = self.get_hallucination()
            for index in self.index_name:
                data = [index, self.index_name[index]]
                if index in index_main_category_count:
                    get_sort = sorted(index_main_category_count[index].items(), key=lambda x: x[1], reverse=True)
                    category_sorted = sorted(get_index_category_list[index].items(), key=lambda x: x[1], reverse=True)
                    data += [get_sort[0][0] + ' ' + '(' + str(index_main_category_count[index][get_sort[0][0]]) + ')',
                             str(get_index_category_list[index][category_sorted[0][0]] /
                                 sum(get_index_category_list[index][key] for key in get_index_category_list[index])),
                             category_sorted[0][0]]
                    csv_writ.writerow(data)
                else:
                    data += ['', '', '', '', '']
                    csv_writ.writerow(data)


class GPTKnowledge(object):
    def __init__(self, input_filepath, input_save_path, times, api_key):
        self.input_filepath = input_filepath
        self.input_save_path = input_save_path
        self.times = int(times)
        self.api_key = api_key

    def get_knowledge_answer(self, input_content):
        url = 'https://fastgpt.aiown.top/api/v1/chat/completions'
        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json'
        }
        data = {
            "chatId": "",
            "stream": False,
            "detail": True,
            "messages": [
                {
                    "content": input_content,
                    "role": "user"
                }
            ]
        }
        response = requests.post(url, headers=headers, json=data)
        # return response.json()['choices'][0]['message']['content']
        return response.json()

    def self_main(self):
        for i in range(self.times):
            save_path = self.input_save_path + '\\' + 'GPT_answer_%s' % str(i + 1)
            save_path_full_record = self.input_save_path + '\\' + 'GPT_answer_full_record_%s' % str(i + 1)
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            if not os.path.exists(save_path_full_record):
                os.makedirs(save_path_full_record)
            get_df = pd.read_excel(self.input_filepath)
            get_name_list = get_df['IUPAC_name']
            get_index_list = [str(x) for x in get_df['Index']]
            name_index = dict(zip(get_name_list, get_index_list))
            for name in name_index:
                get_save_path = os.path.join(save_path, str(name_index[name]) + '.txt')
                get_full_record_save_path = os.path.join(save_path_full_record, str(name_index[name]) + '.txt')
                get_answer_full_record = 'failed'
                try:
                    get_answer_full_record = self.get_knowledge_answer(name)
                    get_answer = get_answer_full_record['choices'][0]['message']['content']
                except:
                    get_answer = 'failed'
                if get_answer != 'failed':
                    with open(get_save_path, 'w', encoding='utf-8') as w:
                        w.write(get_answer)
                if get_answer_full_record != 'failed':
                    with open(get_full_record_save_path, 'w', encoding='utf-8') as w:
                        w.write(str(get_answer_full_record))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.band()

    def band(self):
        self.ui.start.clicked.connect(self.start_gpt_category)
        self.ui.clean_api_key.clicked.connect(self.clean_api_key)
        self.ui.clean_input_filepath.clicked.connect(self.clean_filepath)
        self.ui.clean_output_process.clicked.connect(self.clean_output)
        self.ui.clean_save_path.clicked.connect(self.clean_save_path)
        self.ui.evaluate_GPT.clicked.connect(self.evaluate_gpt)
        self.ui.output_file.clicked.connect(self.output_category_outcome)

    def start_gpt_category(self):
        input_filepath = self.ui.input_filepath.text()
        input_save_path = self.ui.input_save_path.text()
        input_times = self.ui.input_times.text()
        input_core_num = self.ui.input_core_num.text()
        input_api_key = self.ui.input_api_key.text()
        category_mode = self.ui.input_type.currentText()
        if category_mode == 'Zero-Shot':
            gpt_classification = GptMultiprocess(input_filepath, input_save_path, 'zero', input_times,
                                                 input_core_num, input_api_key)
            gpt_classification.self_main()
        elif category_mode == 'Few-Shot':
            gpt_classification = GptMultiprocess(input_filepath, input_save_path, 'few', input_times,
                                                 input_core_num, input_api_key)
            gpt_classification.self_main()
        elif category_mode == 'Knowledge-Database':
            gpt_knowledge = GPTKnowledge(input_filepath, input_save_path, input_times, input_api_key)
            gpt_knowledge.self_main()
        self.ui.output_text.setText('分类完成，相关文件保存在%s路径下，请进行下一步评价分类效果或输出分类结果' % input_save_path)

    def evaluate_gpt(self):
        input_filepath = self.ui.input_filepath.text()
        input_save_path = self.ui.input_save_path.text()
        input_times = self.ui.input_times.text()
        category_mode = self.ui.input_type.currentText()
        # if category_mode == 'Zero-Shot' or category_mode == 'Few-Shot':
        #     evaluate_gpt_function = EvaluateGPT(input_filepath, input_save_path, input_times, False)
        #     evaluate_gpt_function.output_outcome()
        # else:
        #     evaluate_gpt_function = EvaluateGPT(input_filepath, input_save_path, input_times, True)
        #     evaluate_gpt_function.output_outcome()
        self.ui.output_text.setText('评价分类效果完成，相关文件保存在%s路径下，可以进行输出分类结果' % input_save_path)

    def output_category_outcome(self):
        input_filepath = self.ui.input_filepath.text()
        input_save_path = self.ui.input_save_path.text()
        input_times = self.ui.input_times.text()
        category_mode = self.ui.input_type.currentText()
        # if category_mode == 'Zero-Shot' or category_mode == 'Few-Shot':
        #     output_category_function = GetGPTOutcome(input_filepath, input_save_path, input_times, False)
        #     output_category_function.output_outcome()
        # else:
        #     output_category_function = GetGPTOutcome(input_filepath, input_save_path, input_times, True)
        #     output_category_function.output_outcome()
        self.ui.output_text.setText('输出分类结果完成，相关文件保存在%s路径下' % input_save_path)

    def clean_api_key(self):
        self.ui.input_api_key.setText('')

    def clean_filepath(self):
        self.ui.input_filepath.setText('')

    def clean_save_path(self):
        self.ui.input_save_path.setText('')

    def clean_output(self):
        self.ui.output_text.setText('')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

