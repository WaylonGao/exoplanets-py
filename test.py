import lightkurve as lk
import numpy as np
import csv
import matplotlib.pyplot as plt



def fetch_all_kepler_data1(kepler_id):
    #Append the data to CSV
    f=open("keplerData.csv")
    w = csv.writer(f)
    
    # Search for all available TPFs using the Kepler ID
    search_result = lk.search_targetpixelfile(kepler_id, mission='Kepler')
    
    # List to store flux arrays
    flux_arrays = []
    
    # Loop through each search result and download the TPF
    for tpf_file in search_result:
        tpf = tpf_file.download()
        
        # Plot the target pixel file
        #tpf.plot()
        
        # Extract the light curve
        
        lc = tpf.to_lightcurve()
        
        # Append the flux array to the list
        flux_arrays.append(lc.flux)
    
    # Print the flux arrays
    for i, flux in enumerate(flux_arrays):
        print(f"Flux array for TPF {i+1}:")
        for f in flux:
            w.writerow(f)
    print("CSV File data written successfully")


def fetch_all_kepler_data3(kepler_id):
    # Open the CSV file in write mode
    with open("keplerData.csv", mode='w', newline='') as f:
        w = csv.writer(f)
        
        # Search for all available TPFs using the Kepler ID
        search_result = lk.search_targetpixelfile(kepler_id, mission='Kepler')
        
        # List to store flux arrays
        flux_arrays = []
        
        # Loop through each search result and download the TPF
        for tpf_file in search_result:
            tpf = tpf_file.download()
            
            # Extract the light curve
            lc = tpf.to_lightcurve()
            
            # Append the flux array to the list
            flux_arrays.append(lc.flux)
        
        # Write the flux arrays to the CSV file
        for i, flux in enumerate(flux_arrays):
            print(f"Flux array for TPF {i+1}:")
            for f in flux:
                w.writerow([f])

def fetch_all_kepler_data(kepler_id):
    # Open the CSV file in write mode
    with open("keplerData.csv", mode='w', newline='') as f:
        w = csv.writer(f)
        
        # Search for all available TPFs using the Kepler ID
        search_result = lk.search_targetpixelfile(kepler_id, mission='Kepler')
        
        # List to store flux arrays
        flux_arrays = []
        
        # Loop through each search result and download the TPF
        for tpf_file in search_result:
            tpf = tpf_file.download()
            
            # Extract the light curve
            lc = tpf.to_lightcurve()
            
            # Append the flux array to the list
            flux_arrays.append(lc.flux)
        
        # Write the flux arrays to the CSV file
        for i, flux in enumerate(flux_arrays):
            print(f"Flux array for TPF {i+1}:")
            for f in flux:
                # Convert the flux value to a float and write to CSV
                w.writerow([f.value])


def plot_kepler_data(csv_file):
    # Read the data from the CSV file
    flux_values = []
    with open(csv_file, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            flux_values.append(float(row[0]))
    
    # Plot the data using matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(flux_values, label='Flux')
    plt.xlabel('Data Point Index')
    plt.ylabel('Flux Value')
    plt.title('Kepler Flux Data')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
#kepler_id = 11446443  # Replace with your Kepler Object ID

#fetch_all_kepler_data(kepler_id)


#plot_kepler_data('keplerData.csv')

pixelfile = lk.search_targetpixelfile("11446443", quarter=16).table
#pixelfile.plot(frame=1)
#plt.show()
print(pixelfile)

