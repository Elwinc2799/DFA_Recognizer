from flask import Flask, render_template, request
import DFA_Recognizer

# Initialize flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Accept uploaded text file
        uploaded_file = request.files['text_file']

        if uploaded_file:
            text = uploaded_file.read().decode('utf-8')
        else:
            text = """The Echoes of Lost Time" is an epic tale of discovery, conflict, and survival. It starts with 
                        David, a famous explorer, assembling a team of fifteen experts to venture into an uncharted 
                        region rumored to hide the remains of a lost civilization. With Sarah, Ethan, Vanessa, Carl, 
                        Mia, Josh, Emily, Leo, Isabella, Benjamin, Grace, Jacob, Sophia, and Liam on his side, David 
                        embarks on the journey of a lifetime.

                        They arrive at the edge of the unexplored region filled with excitement and a sense of 
                        camaraderie. Carl, the archeologist, feels a sense of anticipation, knowing that they stand on 
                        the brink of a discovery that could redefine history. Mia, the youngest member, is buzzing with 
                        energy, eager to decipher any languages they might encounter.

                        Their journey, however, is not easy. They face their first challenge when a sudden storm hits 
                        their camp. Ethan and Leo work together to protect their equipment, while Sarah coordinates the 
                        team to secure the camp. Vanessa shows her mettle, tending to those injured in the storm.

                        In the aftermath of the storm, Emily discovers a strange artifact, leading them to an ancient 
                        cave. Isabella's geological analysis suggests that the cave might have been a dwelling place for 
                        the ancient civilization. Benjamin and Jacob provide insights about the unique plant life and 
                        animal remains found in the cave.

                        But their joy is short-lived when a sudden cave-in traps them inside. Josh and Leo work 
                        tirelessly to clear the debris, while Grace keeps the morale high, reminding everyone that they 
                        are still on course. Liam steps up to calm the group, using his psychological expertise to 
                        prevent panic.

                        In a moment of tension, a disagreement arises between Ethan and Josh about the best way to 
                        escape, leading to a heated argument. Sarah steps in, reminding them of the importance of their 
                        mission and the need for unity. With her intervention, they finally come to a consensus, 
                        and with a plan in place, they manage to escape the cave.

                        On their exit, they are met by a group of locals who are initially hostile. Sophia uses her 
                        anthropological skills to understand their culture and customs, and Mia uses her language skills 
                        to communicate with them. Gradually, they earn the locals' trust and respect.

                        The climax of the story unfolds as they discover an ancient city, hidden deep within the 
                        jungle, a testament to the lost civilization they were seeking. The team works together to 
                        document their findings, with Emily, Carl, and Sophia taking the lead.

                        They face a final challenge when they realize that their actions have disturbed the local 
                        wildlife. Jacob's biological expertise comes in handy as he devises a plan to restore the 
                        balance, ensuring their discovery does not harm the local ecosystem.

                        Jacob's plan involves a careful relocation of the displaced wildlife and the restoration of 
                        their natural habitats. It's a tricky operation, but with Vanessa and Benjamin assisting him, 
                        they manage to start the process. However, tensions rise when a few of the animals react 
                        aggressively to their efforts.

                        Josh, with his strength and quick reflexes, steps in to protect the team. However, 
                        in the process, he gets injured. Vanessa, the team's medic, quickly jumps into action, 
                        treating his wounds, while the rest of the team works to keep the animals at bay.

                        During this chaotic time, Mia discovers inscriptions on the city's walls that suggest an 
                        ancient ritual to appease the local wildlife. With Sophia's help, they manage to decipher the 
                        ritual and, with the help of the locals, perform it. To everyone's surprise, the ritual 
                        works. The animals calm down, and a sense of peace settles over the area.

                        With the immediate danger averted, the team focuses on documenting their findings and restoring 
                        the balance they had unintentionally disturbed. Carl, Emily, and Isabella work diligently, 
                        cataloguing the artifacts and taking numerous photographs of the ancient city, while Ethan and 
                        Leo use their tech skills to create a 3D model of the city.

                        In the midst of all this, David, Sarah, and Grace negotiate with the local leaders to 
                        establish a preservation plan for the city and its surrounding area. They make sure to 
                        involve the locals in the process, giving them agency over their own heritage.

                        As the expedition nears its end, Liam, the psychologist, recognizes the toll the journey has 
                        taken on the team. He organizes group sessions where they share their experiences, fears, 
                        and triumphs, bringing them closer and reinforcing their bond.

                        The story ends with the team leaving the ancient city, their hearts filled with a mix of triumph 
                        at their discovery and a sense of loss at leaving behind a place that has become a part of them. 
                        They promise to protect the secrets of the city and its history, ensuring that their discovery 
                        benefits the locals and the academic community but does not disrupt the delicate balance of the 
                        ecosystem.

                        "The Echoes of Lost Time" concludes with a bittersweet farewell, as the team returns to their 
                        regular lives, forever changed by their shared journey into the unknown. The bonds they 
                        forged, the challenges they overcame, and the discoveries they made will forever echo in 
                        their hearts and minds."""

        # Split patterns to search by comma, if no pattern input used default list
        if request.form['patterns'] == "":
            patterns = ["David", "Sarah", "Ethan", "Vanessa", "Carl", "Mia", "Josh", "Emily", "Leo", "Isabella",
                        "Benjamin", "Grace", "Jacob", "Sophia", "Liam"]
        else:
            patterns = request.form['patterns'].split(',')

        # Process the text and patterns using the DFA_Recognizer functions
        results = DFA_Recognizer.process_text(text, patterns)

        # Display output to results.html
        return render_template('results.html', results=results)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
