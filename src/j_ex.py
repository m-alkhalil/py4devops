import json
import pandas as pd
import matplotlib.pyplot as plt

#lst[count][main][temp]

with open('set.json','r') as file:
    di=json.load(file)

#print(di['list'])
final = {}
lst = di['list']
#print(di['list'][1]['main']['temp'])


for item in lst:
    final[item['dt_txt']] = {
                    'Temp':item['main']['temp'],
                    'Weather_Status':item['weather'][0]['main']}
# for key in final:
#     print(key, ": ",final[key])#f" Date and Time: {item['dt_txt']}, Temp: {item['main']['temp']}, weather status: {item['weather'][0]['main']}")

def draw_temp_plot(frm) -> None:
    """ This function plot data 
    frm: data frame object
    """

    # Plot the temperature over time (use the index as the x-axis)
    plt.figure(figsize=(10,6))
    plt.plot(frm.index, frm['Temp'],marker='o', color='b', label='Temp (F)')

    plt.title('Tempreture in 5 days')
    plt.xlabel('Date')
    plt.ylabel('Temp (F) ')

    # Display grid and legend
    plt.grid(True)
    plt.legend()

    plt.xticks(rotation=45) # Rotate the x-axis labels for better readability
   # plt.tight_layout() # Adjust the layout to avoid overlap
    plt.show()

df = pd.DataFrame.from_dict(final ,orient='index')
df.index = pd.to_datetime(df.index)
print(df)
draw_temp_plot(df)

