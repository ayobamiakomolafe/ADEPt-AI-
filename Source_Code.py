# A dictionary of drug forms
drug_form_dict={'Injection':'injection','Tablet': 'Tablet', 'Gel':'gel','Bath Additive': 'bath additive',
       'Cutaneous Patch':'cutaneous patch', 'Prolonged-Release Tablet':'prolonged-release tablet',
       'Infusion':'infusion', 'Extended Release Tablet':'extended release'}

# A dictionary of Administration routes
adm_routes_dict={'Subcutaneous': '058', 'Oral': '048', 'Intravenous (otherwise not specified)': 
'042', 'Unknown': '065', 'Intravenous drip': '041', 'Sublingual': '060', 'Intramuscular': '030', 
'Cutaneous': '003', 'Intradermal': '023', 'Subconjunctival': '057', 'Other': '050', 'Parenteral': '051', 
'Subdermal': '059', 'Intra corpus cavernosum': '011', 'Oropharingeal': '049', 'Topical': '061', 
'Intravenous bolus': '040', 'Transdermal': '062', 'Occlusive dressing technique': '046', 
'Transmammary': '063', 'Iontophoresis': '044', 'Rectal': '054'}

# A dictionary of gender
sex_dict= {'Female':2, 'Male':1}

# A dictionary of countries
country_dict={'United States of America': 'US', 'Colombia': 'CO', 'Canada': 'CA', 'Luxembourg': 'LU', 'Argentina': 'AR', 'United Kingdom': 'GB', 'France': 'FR', 'Mexico': 'MX', 'Brazil': 'BR', 'Chile': 'CL', 'Bulgaria': 'BG', 'Denmark': 'DK', 'Puetro Rico': 'PR', 'United States Minor Outlying Islands': 'UM', 'Peru': 'PE', 'Malaysia': 'MY', 'Germany': 'DE', 'Romania': 'RO', 'Switzerland': 'CH', 'Spain': 'ES', 'Australia': 'AU', 'Portugal': 'PT', 'Ireland': 'IE', 'Taiwan': 'TW', 'Sweden': 'SE', 'Greece': 'GR', 'Estonia': 'EE', 'Italy': 'IT', 'Dominican Republic': 
'DO', 'South Africa': 'ZA', 'Israel': 'IL', 'Netherlands': 'NL', 'Japan': 'JP', 'Uruguay': 'UY', 'Egypt': 'EG', 'Poland': 'PL', 'China': 'CN', 'South Korea': 'KR', 'Belgium': 'BE', 'Slovakia': 'SK', 'Turkey': 'TR', 'Lebanon': 'LB', 'Kuwait': 'KW', 'Qatar': 'QA', 'Vietnam': 'VN', 'Croatia': 'HR', 'Costa Rico': 'CR', 'Norway': 'NO', 
'Hungary': 'HU', 'India': 'IN', 'Pakistan': 'PK', 'Austria': 'AT', 'Russia Federation': 'RU', 'Singapore': 'SG', 'Guatemala': 'GT', 'Finland': 'FI', 'New Zealand': 'NZ', 'Iran': 'IR', 'Czech Republic': 'CZ', 'Saudi Arabia': 'SA', 'Honk Kong': 'HK', 'United Arab Emirates': 'AE', 'Tunisia': 'TN', 'Bahrain': 'BH', 'Indonesia': 'ID'}

# List of drugs
drugs=['ABATACEPT',
 'ACETAMINOPHEN\\HYDROCODONE BITARTRATE',
 'ACTEMRA',
 'ACTHAR',
 'ADALIMUMAB',
 'AFSLAMET 10 MG SOLUZIONE INIETTABILE IN SIRINGA PRE?RIEMPITA',
 'AMBRISENTAN',
 'AMGEVITA',
 'ARAVA',
 'ARTHROTEC',
 'AVSOLA',
 'AZATHIOPRINE.',
 'BARICITINIB',
 'BENEPALI',
 'BENLYSTA',
 'BIO?MANGUINHOS INFLIXIMABE',
 'BRENZYS',
 'BUPRENORPHINE TEVA',
 'CELEBREX',
 'CELECOXIB',
 'CELLCEPT',
 'CERTOLIZUMAB PEGOL',
 'CIMZIA',
 'COSENTYX',
 'CREON',
 'CYCLOSPORINE',
 'DICLOFENAC SODIUM/MISOPROSTOL',
 'DUEXIS',
 'DUPIXENT',
 'ENBREL',
 'ERELZI',
 'ERIVEDGE',
 'ETANERCEPT',
 'FLUORESCITE',
 'FORTEO',
 'GABAPENTIN CAPSULES',
 'GAMMAGARD LIQUID',
 'GOLIMUMAB',
 'H.P. ACTHAR',
 'HADLIMA',
 'HULIO',
 'HUMIRA',
 'HYDROCODONE BITARTRATE AND ACETAMINOPHEN',
 'HYDROXYCHLOROQUINE',
 'HYRIMOZ',
 'ILARIS',
 'IMETH',
 'IMRALDI',
 'INFLECTRA',
 'INFLIXIMAB',
 'KENACORT-A',
 'KEVZARA',
 'KINERET',
 'LEFLUNOMIDE',
 'LETROZOLE',
 'LYRICA',
 'MABTHERA',
 'MEDROL',
 'METHOTREXATE',
 'METHYLPREDNISOLONE.',
 'MYCOPHENOLATE',
 'OLUMIANT',
 'ORENCIA',
 'OTEZLA',
 'OTREXUP',
 'PLAQUENIL',
 'POMALYST',
 'PREDNISOLONE.',
 'PREDNISONE',
 'PROLIA',
 'RASUVO',
 'RAYOS',
 'REMICADE',
 'REMSIMA',
 'RENFLEXIS',
 'REPOSITORY CORTICOTROPIN INJECTION',
 'RHEUMATREX',
 'RINVOQ',
 'RITUXAN',
 'RITUXIMAB',
 'ROACTEMRA',
 'RSO CBD 2:1',
 'RUXIENCE',
 'SALAZOPYRIN',
 'SARILUMAB',
 'SIMPONI',
 'SKYRIZI',
 'STELARA',
 'SULFASALAZINE',
 'TALTZ',
 'TOCILIZUMAB',
 'TOFACITINIB',
 'TRAMADOL HYDROCHLORIDE / BRAND NAME NOT SPECIFIED',
 'TREMFYA',
 'TRUXIMA',
 'TYMLOS',
 'ULTRAM',
 'UPADACITINIB',
 'VIMOVO',
 'VOLTAREN',
 'XELJANZ',
 'ZESSLY']



#import needed Libraries
from catboost import CatBoostClassifier
import streamlit as st
import pickle
from PIL import Image
import pandas as pd
import plotly.express as px



st.set_page_config(page_title='ADEPt-AI (Adverse Drug Effect Predictor - AI)',layout="wide", page_icon='Dependencies/RA.png')

st.markdown("<h1 style='text-align: center; color: black;'>ADEPt-AI (Adverse Drug Effect Predictor - AI)</h1>", unsafe_allow_html=True)
st.markdown('##### By applying a machine learning approach to Rheumatoid Arthritis therapy, \
ADEPt-AI (Adverse Drug Effect Predictor - Artificial Intelligence) aims to improve \
prescription outcomes of Rheumatoid Arthritis drugs by predicting how individual \
patients will respond to medication based on demographic factors.')
st.write('\n')
st.markdown('##### ADEPt-AI iterates over possible combinations of \
adverse drug effects for every patient to predict potential drug interactions. Predictions are made automatically, in real-time, and at a low cost. \
This improves prescribing efficiency, reduces the time for clinical decisions,\
and potentially helps to improve the measurement of quality-adjusted life years(QUALYs).')
img=Image.open('Dependencies/RA.png')

cont = st.container()
with cont:
 st.write('\n')
 st.write('\n')
 img=img.resize((700, 400))
 st.image(img, use_column_width=True)
st.write('\n')
st.write('\n')


# Collecting users Input   
country=st.sidebar.selectbox('Country', sorted(list(country_dict.keys())))
country=country_dict[country]
st.write('\n')
drug=st.sidebar.selectbox('Drug Name', drugs)
st.write('\n')
gender=st.sidebar.radio('Gender', list(sex_dict.keys()))
gender=sex_dict[gender]
st.write('\n')
age=st.sidebar.number_input('Age',min_value=1, max_value=100, step=1)
st.write('\n')
route=st.sidebar.selectbox('Drug Administration Route', sorted(list(adm_routes_dict.keys())))
route=adm_routes_dict[route]
st.write('\n')
drug_form=st.sidebar.selectbox('Drug Form', sorted(list(drug_form_dict.keys()) ))
drug_form=drug_form_dict[drug_form]
st.write('\n')

button=st.sidebar.button('Predict Reactions')

#Loading the encoder pickle files
pkl_file = open('Dependencies/Country.pkl', 'rb')
Country= pickle.load(pkl_file) 
pkl_file.close()

pkl_file = open('Dependencies/Drug.pkl', 'rb')
Drug= pickle.load(pkl_file) 
pkl_file.close()

pkl_file = open('Dependencies/Drug_Form.pkl', 'rb')
Drug_Form= pickle.load(pkl_file) 
pkl_file.close()

pkl_file = open('Dependencies/Route.pkl', 'rb')
Route_of_Administration= pickle.load(pkl_file) 
pkl_file.close()

#Encoding users input for machine learning prediction
country=Country.transform([country])[0]
drug=Drug.transform([drug])[0]
drug_form=Drug_Form.transform([drug_form])[0]
route_of_administration=Route_of_Administration.transform([route])[0]
Data=[country,age,gender,drug,drug_form,route_of_administration]


# Making a Prediction from users Input and Outputing the Result
if button:
 st.markdown("<h1 style='text-align: center; color: black;'>Prediction Result</h1>", unsafe_allow_html=True)
 model= CatBoostClassifier(verbose=0)
 Predictions={}
 for i in ['infection','pain', 'swelling', 'vomiting', 'headache', 'rash', 'nausea', 'pneumonia']:
     path='Dependencies/' + i
     model.load_model(path)
     prediction=model.predict_proba(Data)
     Predictions[i]= prediction
 df=pd.DataFrame(Predictions).T.reset_index()
 df[1]= df[1]*100
 df.sort_values(1, inplace=True)
 df.rename(columns={'index': 'ADVERSE EFFECTS', 1: 'PERCENTAGE PROBABILITY'}, inplace=True)
 df['ADVERSE EFFECTS']=df['ADVERSE EFFECTS'].str.upper()
 fig = px.bar(df, y='ADVERSE EFFECTS', x='PERCENTAGE PROBABILITY',height=800, orientation='h')
 fig.update_layout(font_color="black", font_size=20)
 st.plotly_chart(fig, use_container_width=True)



   
    
    
