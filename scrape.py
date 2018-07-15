import requests

for summary_id in range(1, 11400):
    xml = requests.get(
        'https://www.qualitymeasures.ahrq.gov/summaries/downloadcontent/nqmc-{}?contentType=xml'.format(summary_id))
    if xml.status_code == 200:
        print('Saving summary {}/11399'.format(summary_id))
        file = open('summaries/nqmc-{}.xml'.format(summary_id), "w+")
        file.write(xml.text)
        file.close()
