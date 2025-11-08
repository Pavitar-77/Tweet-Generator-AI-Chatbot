import google.generativeai as genai
import ipywidgets as widgets
from IPython.display import display, Markdown
API_KEY = input("enter gemini api key:")
genai.configure(api_key = API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
API_KEY_input = widgets.Text(
    description = "api_key",
    layout = widgets.Layout(width = "400px")
)

topic_input = widgets.Text(
    description = "Topic",
    layout = widgets.Layout(width = "400px")
)
tone_input = widgets.Dropdown(
    description = "Tone",
    options = ("Professional", "Casual", "Motivational", "Informative"),
    layout = widgets.Layout(width = "400px")
)
audience_input = widgets.Text(
    description = "Audience",
    options = ("Professional", "Casual", "Motivational", "Informative"),
    layout = widgets.Layout(width="400px")
)
hashtag_input = widgets.Text(
    description = "Hashtags",
    layout = widgets.Layout(width = "400px")
)
submit_button = widgets.Button(
    description = "Generate Tweet",
    button_style = "Success",
    tooltip = "Click to generate tweet",
    Layout = widgets.Layout(width="400px")
)
output = widgets.Output()

def generate_tweet(b):
  output.clear_output()
  prompt = f"""
  You are an expert Content Writer generate a tweet about the topic "{topic_input.value}".
  use a tone {tone_input.value}.
  generate tweet for audience {audience_input.value}.
  Include the hashtages {hashtag_input.value}.
  Keep it under 2000 characters
  """
  with output:
    try:
      response = model.generate_content(prompt)
      tweet = response.text.strip()
      display(Markdown (f"### Generated Tweet: \n\n {tweet}"))
    except Exception as e:
      print("Error", e)

submit_button.on_click(generate_tweet)

form = widgets.VBox([
    widgets.HTML(value="<h3> * Tweet Generator Agent</h3>"),
    topic_input,
    tone_input,
    audience_input,
    hashtag_input,
    submit_button,
    output
])

display(form)