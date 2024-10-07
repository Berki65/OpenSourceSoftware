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
    total_en = [40 / 125 * midterm + 60 / 100 * final for (midterm, final) in class_en]

    # TODO) Plot midterm/final scores as points
    plt.figure(figsize=(7, 6))
    plt.scatter(midterm_kr, final_kr, color='red', label='Korean')
    plt.scatter(midterm_en, final_en, color='blue', label='English', marker='+')
    plt.xlim(0, 125)
    plt.ylim(0, 100)
    plt.title('Midterm vs Final Scatter')
    plt.xlabel('Midterm scores')
    plt.ylabel('Final scores')
    plt.grid(True)
    plt.legend()
    plt.text(37, 109, 'Berkay Bentetik - 24170078', fontsize=12, color='black', alpha=1, ha='right')
    plt.savefig('class_score_scatter.png')
    plt.show()


    # TODO) Plot total scores as a histogram
    plt.figure(figsize=(7, 6))
    plt.hist(total_kr, bins=10, alpha=0.5, color='red', label='Korean')
    plt.hist(total_en, bins=10, alpha=0.5, color='blue', label='English')
    plt.legend()
    plt.xlim(0, 100)
    plt.title('Total Score')
    plt.xlabel('Total scores')
    plt.ylabel('The number of students')

    plt.text(30, 16, 'Berkay Bentetik - 24170078', fontsize=12, color='black', alpha=1, ha='right')
    plt.savefig('class_score_hist.png')
    plt.show()
