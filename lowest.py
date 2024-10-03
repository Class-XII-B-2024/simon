import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Welcome Message
print("\nWelcome to the Food Adulteration Analysis Tool!")
menu_data={
    1: "Samples Tested",
    2: "Civil Cases on Food Adulteration",
    3: "Criminal Cases on Food Adulteration",
    4: "Penalties Levied",
    5: "Product Category Distribution",
    6: "Commonly Adulterated Products",
    7: "Samples Tested vs. Adulterated (Line Graph)",
    8: "Percentage of Adulterants Used",
    9: "Highest and Lowest Adulteration Rates",
    10: "Details about Samples by State",
    11: "Exit"
}

# Menu Options as a Series
menu_options = pd.Series(menu_data)

# Display the Menu
print("\nFood Adulteration Analysis Menu:")
print(menu_options)

    # Get User Choice
choice = int(input("\nEnter your choice: "))

# Handle User Choice
if choice == 1:
    # Samples Tested (already defined in your code)
    data = pd.read_csv("C://Users//sherin//Desktop//IP project//samples.csv")
    df = pd.DataFrame(data)
    print(df)
elif choice == 2:
    # Civil Cases (already defined in your code)
    data = pd.read_csv("C://Users//sherin//Desktop//IP project//civil.csv")
    df = pd.DataFrame(data)
    df = df.replace('NA', np.nan)
    print("Civil Cases on Food Adulteration:")
    print(df)
elif choice == 3:
    # Criminal Cases (already defined in your code)
    data = pd.read_csv("C://Users//sherin//Desktop//IP project//criminal cases.csv")
    df = pd.DataFrame(data)
    df = df.replace('NA', np.nan)
    print("Criminal Cases on Food Adulteration:")
    print(df)
elif choice == 4:
    # Penalties Levied (already defined in your code)
    data = {'Year': ['2020', '2021', '2022', '2023'], 'No_of_samples': [69850, 77530, 91570, 88310], 'Percentage_of_non_conforming_samples': [22, 23, 25, 27]}
    df = pd.DataFrame(data)
    print(df)
    data = {'No_of_Cases_Launched': [11200, 12670, 15360, 17600], 'No_of_Cases_of_Conviction': [2300, 2650, 3010, 4380], 'Amount_Raised_by_Penalties_Rs': [146729087, 159834617, 193459153, 239120874]}
    df2 = pd.DataFrame(data)
    print(df2)
elif choice == 5:
    # Product Category Distribution (already defined in your code)
    data = {
        'Product Category': ['Fishery and seafood products', 'Vegetable and vegetable products', 'Fruit and fruit products',
                             'Non-chocolate candy and chewing gum', 'Bakery products/dough/mix/icing',
                             'Spices, flavors, and salts', 'Cheese and cheese products'],
        '1998-2004': [1800, 1300, 900, 700, 600, 500, 400],
        '2005-2013': [2300, 1600, 1200, 900, 800, 700, 600]
    }
    df = pd.DataFrame(data)
    df.plot(kind='barh', x='Product Category', figsize=(10, 6), color=['#1f77b4', '#ff7f0e'], width=0.7)
    plt.title('Product Quantity Distribution (1998-2004 vs 2005-2013)')
    plt.xlabel('Quantity')
    plt.ylabel('Product Category')
    plt.legend(title='Year Range')
    plt.show()
elif choice == 6:
    # Commonly Adulterated Products (already defined in your code)
    slices = [30, 24, 31, 12, 3]
    Category = ['Fruits', 'Vegetables', 'Dairy Products', 'Spices', 'Other Products']
    exp = [0, 0, 0.2, 0, 0]
    plt.pie(slices, labels=Category, startangle=90, explode=exp, shadow=True, autopct='%.1F%%')
    plt.title('Food Adulteration Detection')
    plt.legend()
    plt.show()
elif choice == 7:
    # Samples Tested vs. Adulterated (Line Graph) (already defined in your code)
    categories = ['2011-12', '2012-13', '2013-14']
    values1 = [64593, 69949, 72200]
    values2 = [8247, 10380, 13571]
    values3 = [6845, 5840, 10235]
    x = np.arange(len(categories))
    plt.plot(x, values1, label='No.of Samples Examined', color='green', linestyle='dotted', marker='o')
    plt.plot(x, values2, label='No.of Samples found Non-Conforming', color='purple', linestyle='dotted', marker='o')
    plt.plot(x, values3, label='No.of prosecutions Launched', color='pink', linestyle='dotted', marker='o')
    plt.xlabel('Years')
    plt.xticks(x, categories)
    plt.ylabel('Values')
    plt.title('Samples Tested and Found Adulterated')
    plt.legend()
    plt.show()
elif choice == 8:
    # Percentage of Adulterants Used (already defined in your code)
    adulterants = ['Water', 'Urea', 'Starch', 'AR', 'RF', 'Sorbitol', 'Glucose', 'C-Sugar', 'AS', 'Na-Soda', 'S&P',
                   'V. Oil', 'Formalin', 'H202', 'B-Acid', 'Detergent', 'H.Chlorite']
    positive_percentages = [91.0, 27.0, 15.0, 9.0, 24.0, 3.0, 10.0, 31.0, 13.0, 11.0, 19.0, 19.0, 20.0, 15.0, 12.0, 4.0, 5.0]
    plt.figure(figsize=(10, 6))# Adjust figure size as needed
    plt.bar(adulterants, positive_percentages,align='edge', color='skyblue',width=1,edgecolor='black')
    plt.xlabel('Adulterant')
    plt.ylabel('Positive (%)')
    plt.title('Percentage of Adulterants used in the foods')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
elif choice == 9:
    data = {
    'States': ["UP", "Punjab", "Tamil Nadu", "Maharashtra", "J&K"],
    'Failed samples': [8375, 3053, 2461, 1532, 992],
    'Samples tested': [19063, 11057, 7383, 9022, 3643],
    'Convictions': [3237, 22, 896, 83, 310]
    }
df = pd.DataFrame(data)
df.plot('States',kind='bar', figsize=(10, 6), color=['pink', 'purple','cyan'], width=0.7)
plt.title('Details about the samples of adulterants Statewise)')
plt.xlabel('States')
plt.ylabel('Samples')
plt.legend()
plt.show()
