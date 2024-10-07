"""
Assignment from Berkay Bentetik - 24170078
Python Lab 04 - Midterm and Final Exam Visualization
"""

import matplotlib.pyplot as plt

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'): # If 'line' is not a header
                data.append([int(word) for word in line.split(',')])
    return data

if __name__ == '__main__':
    # Load score data
    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    # Read both Korean and English class scores
    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40 / 125 * midterm + 60 / 100 * final for (midterm, final) in class_kr]
    midterm_en, final_en = zip(*class_en)
    total_en = [40 / 125 * midterm + 60 / 100 * final for (midterm, final) in class_en]

    # --- Scatter Plot ---
    # Create a figure and set up the plot
    plt.figure(figsize=(7, 6))
    plt.scatter(midterm_kr, final_kr, color='red', label='Korean')
    plt.scatter(midterm_en, final_en, color='blue', label='English', marker='+')

    #Limit for x and y-axis
    plt.xlim(0, 125)
    plt.ylim(0, 100)

    # Labeling
    plt.title('Midterm vs Final Scatter')
    plt.xlabel('Midterm scores')
    plt.ylabel('Final scores')

    # Add grid
    plt.grid(True)

    # Add legend
    plt.legend(loc= 'upper left')

    # Add watermark text
    plt.text(28, 107, 'Berkay Bentetik - 24170078', fontsize=10, color='black', alpha=1, ha='right')

    # Save and show the plot
    plt.savefig('class_score_scatter.png')
    plt.show()


    # --- Histogram Plot ---
    # Create a figure and set up the plot
    bins = range(0, 105, 5)
    plt.figure(figsize=(7, 6))
    plt.hist(total_kr, bins=bins, alpha=1, color='red', label='Korean')
    plt.hist(total_en, bins=bins, alpha=0.3, color='blue', label='English')

    # Limit for x-axis
    plt.xlim(0, 100)

    # Labeling
    plt.title('Midterm vs Final Histogram')
    plt.xlabel('Total scores')
    plt.ylabel('The number of students')

    # Add legend
    plt.legend(loc='upper left')

    # Add watermark text
    plt.text(22, 9, 'Berkay Bentetik - 24170078', fontsize=10, color='black', alpha=1, ha='right')

    # Save and show the plot
    plt.savefig('class_score_hist.png')
    plt.show()
