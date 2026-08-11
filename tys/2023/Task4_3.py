from flask import *

app = Flask("__main__")

@app.route('/')
def home():
    data = []
    f = open("decompressedimage.txt", 'r')

    for line in f:
        line = line.strip()
        data.append(line)

    print(data)

    colors = {
            "000" : "red",
            "001" : "white",
            "010" : "yellow",
            "011" : "blue",
            "100" : "black",
            "110" : "green"

        }
    
    box = []
    
    for row_num in range(9):
        row = []
        
        for col in range(9):
            index = col + 9 * row_num
            color = colors[data[index]]
            print(color)
            row.append(color)
            
        box.append(row)

    print(box)

    
    return render_template("Task4_3.html", box = box)

if __name__ == "__main__":
    app.run()
