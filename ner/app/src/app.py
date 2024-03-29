from h2o_wave import main, app, Q, ui, site
import requests

@app('/')
async def home(q: Q):
    if q.args.show_inputs:
        payload = {'sentence': q.args.textbox_required}
        print("here1")
        response = requests.post('http://api:8000/ner', params = payload)
        print("here2")
        r_info = response.json()
        r_dict = r_info['result']
        str = ""
        for ent in r_dict:
            str = str + "\nEntity Type: " + ent["entity"] + ", Name: " + ent["value"] + "\n"

        q.page['result'] = ui.markdown_card(
            box='1 3 10 6',
            title='Result',
            content= str,
        )

    else:
        q.page['home'] = ui.form_card(box='1 1 10 2', items=[
            ui.textbox(name='textbox_required', label='Enter a Sentence', required=True),
            ui.button(name='show_inputs', label='Submit', primary=True),
        ])
    await q.page.save()
