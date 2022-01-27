# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
"""if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if 5 > 2:
 print("Five is greater than two!")
x = 10
print(type(x))

a = 4
A = "Sally"
print(type(A)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = -0.0000001
y = 10
print(x + y)

x = "awesome"
def myfunc():
    global x
    x = 'FANTASTIC'
    print("Python is " + x)
myfunc()
print('Pyhton is ' + x)


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)
"""
"""
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

  print("expensive" not in txt)

class wallet():
  money = 50

  def __len__(self):
    return self.money




w = wallet()
w.money = 0
print(bool(w))


import json

def is_json(jsonCheck):
  try:
      with open(jsonCheck, "r") as read_file:
          data = json.load(read_file)
  except ValueError as e:
    return False
  return True

print(is_json("C:\\Users\\nadezhda.patrusheva\\PycharmProjects\\pythonProject1\\jsonCheck1.json"))
""""


import requests
query = {'ServiceAccountId':'700006917'}
response = requests.get("https://allinone-ota.api.nutsservices.nl/api/Fulfillment/Offer/{ServiceAccountId}.json", params=query)
print(response.json())


