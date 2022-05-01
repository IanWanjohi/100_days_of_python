# Functions with Outputs

def format_name(f_name, l_name):
  """Returns correctly punctuated name."""       # Docstrings
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

name = format_name("RUSLAN","MalinovSKY")
print(name)