from flask import Flask, render_template_string, request, send_from_directory

app = Flask(__name__)

# Multi-stream career suggestions
def get_suggestions(user_input):
    user_input = user_input.lower()

    # Tech / CSE
    if "frontend" in user_input:
        return "Learn HTML, CSS, JavaScript → Then go for React & Next.js."
    elif "backend" in user_input:
        return "Start with Python/Java, then learn Flask/Django or Node.js."
    elif "data" in user_input or "ai" in user_input:
        return "Learn Python, Pandas, ML basics → Then try TensorFlow or PyTorch."

    # Engineering non-CSE
    elif "mechanical" in user_input or "robotics" in user_input:
        return "Learn Arduino, SolidWorks, ROS basics."
    elif "ece" in user_input or "electronics" in user_input:
        return "Learn embedded systems, IoT basics, PCB design."
    elif "civil" in user_input:
        return "Learn AutoCAD, STAAD Pro, project management basics."

    # Commerce / Management / Arts
    elif "commerce" in user_input or "finance" in user_input:
        return "Learn Excel, Accounting Software, Financial Modelling basics."
    elif "mba" in user_input or "management" in user_input:
        return "Learn Business Analytics, Marketing, Leadership & Communication."
    elif "arts" in user_input or "design" in user_input:
        return "Learn Adobe Suite, Figma, Graphic & UI/UX Design fundamentals."

    # Generic
    else:
        return "Explore general skills: Communication, Problem-solving, Time Management, Git/GitHub."

# Serve CSS manually (flat folder)
@app.route("/style.css")
def serve_css():
    return send_from_directory(".", "style.css")

# Load HTML from file
def load_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route("/", methods=["GET", "POST"])
def index():
    suggestion = None
    if request.method == "POST":
        user_input = request.form["career_input"]
        suggestion = get_suggestions(user_input)
    html = load_html()
    return render_template_string(html, suggestion=suggestion)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render assigns PORT automatically
    app.run(host="0.0.0.0", port=port, debug=True)
