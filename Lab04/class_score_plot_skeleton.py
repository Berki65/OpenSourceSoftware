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

    # TODO) Prepare midterm, final, and total scores
    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40/125*midterm + 60/100*final for (midterm, final) in class_kr]
    midterm_en, final_en = zip(*class_en)
    total_en = [40/125*midterm + 60/100*final for (midterm, final) in class_en]

    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    # TODO) Plot midterm/final scores as points
    ax[0].scatter(midterm_kr, final_kr, color='red', label='Korean')
    ax[0].scatter(midterm_en, final_en, color='blue', label='English')
    ax[0].set_xlim(0, 125)
    ax[0].set_ylim(0, 100)
    ax[0].set_title('Midterm vs Final')
    ax[0].set_xlabel('Midterm')
    ax[0].set_ylabel('Final')
    ax[0].grid(True)
    ax[0].legend()


    # TODO) Plot total scores as a histogram
    ax[1].hist(total_kr, bins=10, alpha=0.5, color='red', label='Korean')
    ax[1].hist(total_en, bins=10, alpha=0.5, color='blue', label='English')
    ax[1].legend()
    ax[1].set_xlim(0, 100)
    ax[1].set_title('Total Score')
    ax[1].set_xlabel('Total')
    ax[1].set_ylabel('Frequency')

    plt.show()