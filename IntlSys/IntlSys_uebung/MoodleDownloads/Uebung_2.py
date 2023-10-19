#!/usr/bin/env python
# coding: utf-8

# # Übung 2: Daten
# Die Einführung zu Python erfogt direkt an einem praktischen Beispiel. Über <https://www.kaggle.com/> können eine vielzahl von Datensätzen für maschinelles Lernen bezogen werden. 
# 
# Die meisten davon sind schon aufbereitet und direkt nutzbar. Z.B. dieser: <https://www.kaggle.com/datasets/mkoklu42/pumpkin-seeds-dataset> den wir für Sie in Ihrem Arbeitsbereich unter ```shared_data/Pumpkin_Seeds_Dataset/``` abgelegt haben.
# 
# Der Datensatz enthält 2500 Einträge mit jeweils 12 Merkmalen, die die Eigenschaften von zwei unterschiedlichen Sorten von Kürbuissamen beschreiben. Details dazu können Sie in der dazugehörigen Veröffentlichung nachlesen: [Koklu2021](https://link.springer.com/content/pdf/10.1007/s10722-021-01226-0.pdf)(das PDF liegt auch im Verzeichnis mit den Daten). Die folgenden Bilder sind dieser Veröffentlichung entnommen. 
# 
# Bildaufnahmen der beiden Sorten, wie die untern Dargestellten, wurden verwendet um die 12 Eigenschaften zu extrahieren. 
# ![image-3.png](attachment:image-3.png)
# 
# Einige der Eigenschaften, illustriert am Beispiel eines Kürbiskerns: 
# ![image-2.png](attachment:image-2.png)
# 
# Eine mögliche Fragestellung für maschinelles Lernen könnte sein: Lassen sich die beiden Sorten anhand der 12 Merkmale eindeutig voneinander unterscheiden? Ein mögliches Anwendungszenario könnte dann eine Sortiermaschine für Kürbissaat sein.

# ## Aufgabe 1
# Laden Sie den Datensatz mit Python und überprüfen Sie die Eigenschaften der Daten (z.B. Anzahl der Datenpunkte, Anzahl der Merkmale je Datenpunkt, Anzahl der Klassen, Anzahl der fehlenden Werte, etc.)

# ### Lösungsmöglichkeit 1
# Nutzen Sie [pandas](https://pandas.pydata.org/) um die Exceldatei ```Pumpkin_Seeds_Dataset.xlsx``` in einen Pandas [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) zu laden.

# In[ ]:


# Hier Ihre Lösung


# ### Lösungsmöglichkeit 2
# Nutzen Sie [SciPy](https://scipy.org/) um die arff-Datei ```Pumpkin_Seeds_Dataset.arff``` zu laden (und wandeln Sie die geladenenen Daten in einen Pandas [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)). 

# In[ ]:


# Hier Ihre Lösung


# # Aufgabe 2
# Vergleichen Sie die beiden DataFrames aus Aufgabe 1. Sind die Daten in der Exceldatei identisch zu denen in der Arff-Datei? (Das wäre zu erwarten, schlißelich ist es dieselbe Quelle, aber sicher ist sicher...)

# In[ ]:


# Hier Ihre Lösung

