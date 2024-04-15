# Start main program to provide a selection menu as an interface with the WCPS Server

import subprocess

def program_b():
    print("Executing program B...")
    # Add your code for program B here

def display_menu():
    print("Selction Menu as an interface with the WCPS Server:")
    print("1. WCPS query to access and encode the datacube into a jpeg image")
    print("2. WCS request to subset the datacube")
    print("3. WCPS query with fusion of different coverages")
    print("4. WCPS query to retrieve minimum temperature of Bremen City in 2014")
    print("5. WCPS query to retrieve maximum temperature of Bremen City in 2014")
    print("6. WCPS query to retrieve average temperature of Bremen City in 2014")
    print("7. WCPS query to retrieve monthly average temperature of Bremen City in 2014 -NOT started")
    print("8. Quit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            try:
                completed_process = subprocess.run(["python", "opt1_wcps_access.py"],capture_output=True,text=True)
                if completed_process.returncode == 0:
                    print("==============================")
                    print("execution sucessful")
                    print(completed_process.stdout)
                else:
                    print("==============================")
                    print("error in execution")
                    print(completed_process.stderr)
            except FileNotFoundError:
                print("Error: opt1_wcps_access.py not found.")
        elif choice == "6":
            try:
                completed_process = subprocess.run(["python", "opt6_wcps_average.py"],capture_output=True,text=True)
                if completed_process.returncode == 0:
                    print("==============================")
                    print("execution sucessful")
                    print(completed_process.stdout)
                else:
                    print("==============================")
                    print("error in execution")
                    print(completed_process.stderr)
            except FileNotFoundError:
                print("Error: opt6_wcps_average.py not found.")
        elif choice == "8":
            print("==============================")
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()