import pulp

model = pulp.LpProblem("Maximize production", pulp.LpMaximize)

lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit juice", lowBound=0, cat='Integer')

model += lemonade + fruit_juice, "Total production"

model += 2 * lemonade + 1 * fruit_juice <= 100, "Water Constraint"
model += 1 * lemonade <= 50, "Sugar constraint"
model += 1 * lemonade <= 30, "Lemon juice constraint"
model += 2 * fruit_juice <= 40, "Fruit puree constraint"

model.solve()

lemonade_qty = lemonade.varValue
fruit_juice_qty = fruit_juice.varValue
total_production = pulp.value(model.objective)

print(f"Lemonade: {lemonade_qty}")
print(f"Fruit juice: {fruit_juice_qty}")
print(f"Total production: {total_production}")
