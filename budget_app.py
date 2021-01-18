import math
import itertools

class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.maxDiff = None

  def deposit(self, amount, description = ''):
    amount = float(amount)
    deposit_dict = {'amount': amount,
    'description': description}
    self.ledger.append(deposit_dict)
    return print(deposit_dict)

  def withdraw(self, amount, description = ''):
    amount = float(amount)
    if self.check_funds(amount) == False:
      return False
    else:
      withdrawal_dict = {'amount': -amount, 'description': description}
      self.ledger.append(withdrawal_dict)
    return True

  def get_balance(self):
    final_balance = 0
    for i in range(len(self.ledger)):
      final_balance += self.ledger[i]['amount']
    return final_balance
  
  def transfer(self, amount, new_category):
    if self.check_funds(amount) == False:
      return False
    else:
      amount = float(amount)
      withdrawal_desc = f'Transfer to {new_category.name}'
      deposit_desc = f'Transfer from {self.name}'
      withdrawal_dict = {'amount': -amount, 'description': withdrawal_desc}
      deposit_dict = {'amount': amount, 'description': deposit_desc}
      self.ledger.append(withdrawal_dict)
      new_category.ledger.append(deposit_dict)
    return True

  def check_funds(self, amount):
    amount = float(amount)
    final_balance = 0
    for i in range(len(self.ledger)):
      final_balance += self.ledger[i]['amount']
    if amount > final_balance:
      return False
    else:
      return True
  
  def __str__(self):
    category_name = str(self.name)
    initial_text = category_name.center(30, '*')
    final_text = initial_text + '\n'
    for i in self.ledger:
      final_text += f"{i['description'][:23].ljust(23)}{format(i['amount'], '.2f').rjust(7)}" + '\n'
    final_text += f"Total: {format(self.get_balance(), '.2f')}"
    return final_text

def round_down(x):
    return int(math.floor(x / 10.0)) * 10


    

def create_spend_chart(categories):
  chart_text = 'Percentage spent by category' + '\n'
  total_withdrawal = 0
  percentage_per_category = []
  total_category = []
  filtered_withdrawals = []
  names_list = []
  lines_chart = '    ' + ('-' * 10) + '\n'
  for i in categories:
    for k in i.ledger:
      if k['amount'] < 0:
        total_withdrawal += k['amount']
  for z in categories:
    result = [x for x in z.ledger if x['amount'] < 0]
    filtered_withdrawals.append(result)
  for y in filtered_withdrawals:
    sum_expenses = sum(item['amount'] for item in y)
    total_category.append(sum_expenses)
  for w in range(len(total_category)):
    percentage_per_category.append(round_down((total_category[w]/total_withdrawal)*100))
  
  number_of_chart = 100
  while number_of_chart >= 0:
    chart_text += str(number_of_chart).rjust(3) + '|' + ' '
    for b in range(len(percentage_per_category)):
      if percentage_per_category[b] >= number_of_chart:
        chart_text += 'o' + '  '
      else:
        chart_text += '   '
    number_of_chart -= 10
    chart_text += '\n'
  chart_text += lines_chart
  for t in categories:
    names_list.append(t.name)

  for i in itertools.zip_longest(*names_list, fillvalue = ' '):
    if any(j != ' ' for j in i):
      chart_text += '     ' + '  '.join(i) + '  ' + '\n'
      
  return chart_text.rstrip() + '  '