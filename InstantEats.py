import datetime
import os

navigator_symbol = "/"
if os.name == "nt":
    navigator_symbol = "\\"


class Default:
    def __init__(self, list_foods, list_drinks, var_discount_1 ,list_item_price, var_discount_2 ,
                 var_discount_3, var_discount_1_rate, var_discount_2_rate, var_discount_3_rate, list_item_order):
        self.list_foods = list_foods
        self.list_drinks = list_drinks
        self.list_item_price = list_item_price
        self.var_discount_1 = var_discount_1
        self.var_discount_2 = var_discount_2
        self.var_discount_3 = var_discount_3
        self.var_discount_1_rate = var_discount_1_rate
        self.var_discount_2_rate = var_discount_2_rate
        self.var_discount_3_rate = var_discount_3_rate
        self.list_item_order = list_item_order


class Main(Default):

    def def_default(self):
        global list_drinks, list_foods, list_item_order, list_item_price

    def def_main(self):
        while True:
            print("*" * 23 + " Welcome to Instant Eats " + "*" * 24 + "\n")
            print("*" * 29 + " MAIN MENU " + "*" * 32 + "\n"
                                                        "\t(O) ORDER\n"
                                                        "\t(T) TRANSACTION HISTORY\n"
                                                        "\t(E) EXIT\n" +
                  "_" * 72)

            input_1 = str(input("Please Select Your Operation: ")).upper()
            if len(input_1) == 1:
                if input_1 == 'O':
                    print("\n" * 2)
                    self.def_order_menu()
                    break
                elif input_1 == 'T':
                    print("\n" * 2)
                    self.def_report()
                    break
                elif input_1 == 'E':
                    print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                    break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

    def def_order_menu(self):
        while True:
            print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"
                                                       "\t(F) FOODS AND DRINKS\n"
                                                       "\t(R) RESET\n"
                                                       "\t(E) EXIT\n" +
                  "_" * 72)

            input_1 = str(input("Please Select Your Operation: ")).upper()
            if len(input_1) == 1:
                if input_1 == 'F':
                    print("\n" * 10)
                    self.def_food_drink_order()
                    break
                elif input_1 == 'R':
                    self.def_main()
                    break
                elif input_1 == 'E':
                    print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                    break
                else:
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

    def def_report(self):
        while True:
            print("*" * 33 + "TRANSACTION" + "*" * 33 + "\n")
            file_report = open('files' + navigator_symbol + 'report.fsd', 'r')
            print(file_report.read())
            print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
            print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
            input_1 = str(input("Please Select Your Operation: ")).upper()
            if input_1 == 'M':
                print("\n" * 10)
                self.def_main()
                break
            elif input_1 == 'E':
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

    def def_payment(self):
        name = str(input("Enter Full Name: "))
        address = str(input("Address: "))
        phone_number = str(input("Enter Phone Number: "))
        print("*" * 32 + " USER DETAILS " + "*" * 33 + "\n")
        print("Full Name:\t", name)
        print("Full Address:\t", address)
        print("Contact Number:\t", phone_number)

        while True:
            print("*" * 32 + " PAYMENT " + "*" * 33 + "\n")
            total_price = 0

            report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(datetime.datetime.now())[
                                                                                       :19] + "\n" + " " * 17 + "-" * 35
            report_new += "\n" + " " * 17 + "FULL NAME: " + name
            report_new += "\n" + " " * 17 + "ADDRESS: " + address
            report_new += "\n" + " " * 17 + "PHONE NUMBER: " + phone_number + "\n" + " " * 17 + "-" * 35

            i = 0
            while i < len(self.list_item_order):
                if self.list_item_order[i] != 0:
                    if (i >= 0) and (i < 40):
                        report_new += "\n" + " " * 17 + str(self.list_foods[i]) + "  x  " + str(self.list_item_order[i])
                        print(" " * 17 + str(self.list_foods[i]) + "  x  " + str(self.list_item_order[i]))
                        total_price += self.list_item_price[i] * self.list_item_order[i]
                    if (i >= 40) and (i < 80):
                        report_new += "\n" + " " * 17 + str(self.list_drinks[i - 40]) + "  x  " + str(
                            self.list_item_order[i])
                        print(" " * 17 + str(self.list_drinks[i - 40]) + "   x  " + str(self.list_item_order[i]))
                        total_price += self.list_item_price[i] * self.list_item_order[i]
                    i += 1
                else:
                    i += 1

            if total_price > self.var_discount_3:
                total_price -= total_price * self.var_discount_3_rate
                report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                                                           "" + " " * 17 + "DISCOUNT RATES:      % " + str(
                    self.var_discount_3_rate * 100) + "\n" \
                                                 "" + " " * 17 + "DISCOUNT AMOUNTS:   P " + str(
                    round(total_price * self.var_discount_3_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                                                                                                "" + " " * 17 + \
                              "TOTAL PRICES:       P " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
                print(" " * 17 + "-" * 35 + "\n"
                                            "" + " " * 17 + "DISCOUNT RATES:      % " + str(
                    self.var_discount_3_rate * 100) + "\n"
                                                 "" + " " * 17 + "DISCOUNT AMOUNTS:   P " + str(
                    round(total_price * self.var_discount_3_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                                                                                                "" + " " * 17 +
                      "TOTAL PRICES:       P " + str(round(total_price, 2)))
            elif total_price > self.var_discount_2:
                total_price -= total_price * self.var_discount_2_rate
                report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                                                           "" + " " * 17 + "DISCOUNT RATES:      % " + str(
                    self.var_discount_2_rate * 100) + "\n" \
                                                 "" + " " * 17 + "DISCOUNT AMOUNTS:   P " + str(
                    round(total_price * self.var_discount_2_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                                                                                                "" + " " * 17 + \
                              "TOTAL PRICES:       P " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
                print(" " * 17 + "-" * 35 + "\n"
                                            "" + " " * 17 + "DISCOUNT RATES:      % " + str(
                    self.var_discount_2_rate * 100) + "\n"
                                                 "" + " " * 17 + "DISCOUNT AMOUNTS:   P " + str(
                    round(total_price * self.var_discount_2_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                                                                                                "" + " " * 17 +
                      "TOTAL PRICES:       P " + str(round(total_price, 2)))
            elif total_price > self.var_discount_1:
                total_price -= total_price * self.var_discount_1_rate
                report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                                                           "" + " " * 17 + "DISCOUNT RATES:      % " + str(
                    self.var_discount_1_rate * 100) + "\n" \
                                                 "" + " " * 17 + "DISCOUNT AMOUNTS:   P " + str(
                    round(total_price * self.var_discount_1_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                                                                                                "" + " " * 17 + \
                              "TOTAL PRICES:       P " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
                print(" " * 17 + "-" * 35 + "\n"
                                            "" + " " * 17 + "DISCOUNT RATES:      % " + str(
                    self.var_discount_1_rate * 100) + "\n"
                                                 "" + " " * 17 + "DISCOUNT AMOUNTS:   P " + str(
                    round(total_price * self.var_discount_1_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                                                                                                "" + " " * 17 +
                      "TOTAL PRICES:       P " + str(round(total_price, 2)))
            else:
                report_new += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       $ " + str(
                    round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
                print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       $ " + str(round(total_price, 2)))

            print("\n (P) PAY           (M) MAIN MENU           (T) TRANSACTION HISTORY          (E) EXIT\n" + "_" * 72)
            input_1 = str(input("Please Select Your Operation: ")).upper()
            if input_1 == 'P':
                print("\n" * 10)
                print("Successfully Paid!")
                file_report = open('files' + navigator_symbol + 'report.fsd', 'a')
                file_report.write(report_new)
                file_report.close()
                self.def_default()
            elif input_1 == 'M':
                print("\n" * 10)
                self.def_main()
                break
            elif input_1 == 'T':
                print("\n" * 10)
                self.def_report()
                break
            elif ('E' in input_1) or ('e' in input_1):
                print("*" * 32 + " Thank you! " + "*" * 31 + "\n")
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

    def def_full_file_reader(self):
        file_foods = open('files' + navigator_symbol + 'list_foods.fsd', 'r')
        for i in file_foods:
            list_foods.append(str(i.strip()))
        file_foods.close()

        file_drinks = open('files' + navigator_symbol + 'list_drinks.fsd', 'r')
        for i in file_drinks:
            list_drinks.append(str(i.strip()))
        file_drinks.close()

        i = 0
        while i <= (len(self.list_foods) - 1):
            if 'P' in self.list_foods[i]:
                self.list_foods[i] = str(self.list_foods[i][:self.list_foods[i].index('P') - 1]) + ' ' * (
                        20 - (self.list_foods[i].index('P') - 1)) + str(self.list_foods[i][self.list_foods[i].index('P'):])
            i += 1

        i = 0
        while i <= (len(self.list_drinks) - 1):
            if 'P' in self.list_drinks[i]:
                self.list_drinks[i] = str(self.list_drinks[i][:self.list_drinks[i].index('P') - 1]) + ' ' * (
                        20 - (self.list_drinks[i].index('P') - 1)) + str(self.list_drinks[i][self.list_drinks[i].index('P'):])
            i += 1

    def def_file_sorter(self):
        global list_foods, list_drinks
        list_foods = sorted(self.list_foods)
        list_drinks = sorted(self.list_drinks)

        i = 0
        while i < len(self.list_foods):
            self.list_item_price[i] = float(self.list_foods[i][int(self.list_foods[i].index("P") + 2):])
            i += 1

        i = 0
        while i < len(self.list_drinks):
            self.list_item_price[40 + i] = float(self.list_drinks[i][int(self.list_drinks[i].index("P") + 2):])
            i += 1

    def def_food_drink_order(self):
        while True:
            print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 26)
            print(" |NO| |FOOD NAME|         |PRICE|   |  |NO| |DRINK NAME|        |PRICE|")

            i = 0
            while i < len(list_foods) or i < len(list_drinks):
                var_space = 1
                if i <= 8:
                    var_space = 2

                if i < len(list_foods):
                    food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[i]) + "  | "
                else:
                    food = " " * 36 + "| "
                if i < len(list_drinks):
                    drink = "(" + str(41 + i) + ")" + " " + str(list_drinks[i])
                else:
                    drink = ""
                print(food, drink)
                i += 1

            print("\n (R) RESET           (P) PAYMENT                     (E) EXIT\n" + "_" * 72)

            input_1 = input("Please Select Your Operation: ").upper()
            if input_1 == 'R':
                print("\n" * 10)
                self.def_main()
                break
            if input_1 == 'E':
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
            if input_1 == 'P':
                print("\n" * 10)
                self.def_payment()
                break
            try:
                int(input_1)
                if ((len(self.list_foods) >= int(input_1) > 0) or (
                        len(self.list_drinks) + 40 >= int(input_1) > 40)):
                    try:
                        print("\n" + "_" * 72 + "\n" + str(self.list_foods[int(input_1) - 1]))
                    except:
                        pass
                    try:
                        print("\n" + "_" * 72 + "\n" + str(self.list_drinks[int(input_1) - 41]))
                    except:
                        pass
                    input_2 = input("How Many You Want to Order?: ").upper()
                    if int(input_2) > 0:
                        self.list_item_order[int(input_1) - 1] += int(input_2)
                        print("\n" * 10)
                        print("Successfully Ordered!")
                        self.def_food_drink_order()
                        break

                    else:
                        print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
            except:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")


if __name__ == "__main__":
    list_foods = []
    list_drinks = []
    list_item_price1 = [0] * 100
    var_discount_1_1 = 200
    var_discount_2_1 = 1000
    var_discount_3_1 = 5000
    var_discount_1_rate1 = 0.05
    var_discount_2_rate1 = 0.10
    var_discount_3_rate1 = 0.15
    list_item_order1 = [0] * 100
    program = Main(list_foods, list_drinks, var_discount_1_1, list_item_price1, var_discount_2_1,
                   var_discount_3_1, var_discount_1_rate1, var_discount_2_rate1, var_discount_3_rate1, list_item_order1)
    program.def_full_file_reader()
    program.def_file_sorter()
    program.def_default()
    program.def_main()