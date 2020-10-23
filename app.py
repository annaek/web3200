from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/browse')
def browse():
    nav = [
        {"name": "Horror", "url": "horror"},
        {"name": "Business", "url": "business"},
        {"name": "Science", "url": "science"},
    ]
    return render_template('browse.html', nav=nav)


@app.route('/browse/<category>')
def category(category):
    categ = [
        {'genre': 'horror',
            "description": '''Horror fiction is fiction in any medium intended to scare,
            unsettle, or horrify the audience. Historically,
            the cause of the "horror" experience has often
            been the intrusion of a supernatural element into
            everyday human experience. Since the 1960s,
            any work of fiction with a morbid, gruesome,
            surreal, or exceptionally suspenseful or
            frightening theme has come to be called "horror".
            Horror fiction often overlaps science fiction or fantasy
            , all three of which
            categories are sometimes placed under
            the umbrella classification speculative fiction.''',
            "url_book1": "horror", "label1": "A Deadly Education",
            "url_book2": "horror", "label2": "When No One is Watching",
            "url_book3": "horror", "label3": "Watch Over Me", },
        {'genre': 'business',
            "description": '''A business (also known as enterprise or firm)
            is an organization engaged in the trade of goods,
            services, or both to consumers. Businesses are
            predominant in capitalist economies, where
            most of them are privately owned and administered
            to earn profit to increase the wealth of their owners.
            Businesses may also be not-for-profit or state-owned.
            A business owned by multiple individuals may be
            referred to as a company, although that term
            also has a more precise meaning.''',
            "url_book1": "business", "label1": "Eat a Peach",
            "url_book2": "business", "label2": "Mill Town:"
            " Reckoning with What Remains",
            "url_book3": "business", "label3": "2030: How Today's Biggest " 
            "Trends Will Collide and Reshape the Future of Everything", },
        {'genre': 'science',
            "description": '''Science (from the Latin scientia, meaning “knowledge”)
            is the effort to discover, and increase human
            understanding of how the physical world works.
            Through controlled methods, science uses observable
            physical evidence of natural phenomena to collect data,
            and analyzes this information to explain what
            and how things work.''',
            "url_book1": "science", "label1": "Interference",
            "url_book2": "science", "label2": "Find Layla: A Novel",
            "url_book3": "science", "label3": "The Overstory", }
    ]
    return render_template('category.html', categ=categ, category=category)


@app.route('/<category>/<book>')
def book(category, book):
    books = [
        {'genre': 'horror',
         'label': 'A Deadly Education',
         'author': 'Naomi Novik',
         'description': '''
            A Deadly Education is set at Scholomance,
            a school for the magically gifted where failure
            means certain death (for real) — until one girl,
            El, begins to unlock its many secrets.
            There are no teachers, no holidays,
            and no friendships, save strategic ones.
            Survival is more important than any letter
            grade, for the school won’t allow its students
            to leave until they graduate… or die!
            The rules are deceptively simple:
            Don’t walk the halls alone.
            And beware of the monsters who lurk everywhere.
            El is uniquely prepared for the school’s dangers.
            She may be without allies, but she possesses
            a dark power strong enough to level mountains
            and wipe out millions. It would be easy
            enough for El to defeat the monsters that
            prowl the school. The problem? Her
            powerful dark magic might also kill
            all the other students'''},
        {'genre': 'horror',
         'label': 'When No One is Watching',
         'author': 'Alyssa Cole',
         'description': '''
            Sydney Green is Brooklyn born and raised,
            but her beloved neighborhood seems to change
            every time she blinks. Condos are sprouting
            like weeds, FOR SALE signs are popping up
            overnight, and the neighbors she’s known
            all her life are disappearing.
            To hold onto her community’s past and present,
            Sydney channels her frustration into a
            walking tour and finds an unlikely and unwanted
            assistant in one of the new arrivals to
            the block—her neighbor Theo.But Sydney and Theo’s
            deep dive into history quickly becomes a
            dizzying descent into paranoia and fear.
            Their neighbors may not have moved to the
            suburbs after all, and the push to revitalize
            the community may be more deadly than advertised.
            When does coincidence become conspiracy?
            Where do people go when gentrification
            pushes them out? Can Sydney and Theo
            trust each other—or themselves—long
            enough to find out before they too disappear?'''},
        {'genre': 'horror',
         'label': 'Watch Over Me',
         'author': 'Nina LaCour',
         'description': '''
            Mila is used to being alone.
            Maybe that’s why she said yes to the opportunity:
            living in this remote place, among the flowers
            and the fog and the crash of waves far below.
            But she hadn’t known about the ghosts. Newly
            graduated from high school, Mila has aged out
            of the foster care system. So when she’s offered
            a job and a place to stay at a farm on an
            isolated part of the Northern California Coast,
            she immediately accepts. Maybe she will finally
            find a new home, a real home. The farm is a refuge,
            but also haunted by the past traumas its young
            residents have come to escape. And Mila’s own
            terrible memories are starting to rise
            to the surface. Watch Over Me is another stunner
            from Printz Award-Winning author Nina LaCour,
            whose empathetic, lyrical prose is at the
            heart of this modern ghost story of
            resilience and rebirth'''},
        {'genre': 'business',
         'label': 'Eat a Peach',
         'author': 'David Chang',
         'description': '''
            In 2004, David Chang opened a noodle
            restaurant named Momofuku in Manhattan's
            East Village, not expecting the business to
            survive its first year. In 2018, he was
            the owner and chef of his own restaurant
            empire, with 15 locations from New York
            to Australia, the star of his own hit
            Netflix show and podcast, was named one
            of the most influential people of the
            21st century and had a following of over
            1.2 million. In this inspiring, honest and
            heartfelt memoir, Chang shares the
            extraordinary story of his culinary
            coming-of-age.
            Growing up in Virginia, the son of Korean immigrant
            parents, Chang struggled with feelings of
            abandonment, isolation and loneliness
            throughout his childhood. After failing to
            find a job after graduating, he convinced
            his father to loan him money to open a restaurant.
            Momofuku's unpretentious air and great-tasting
            simple staples - ramen bowls and pork buns -
            earned it rave reviews, culinary awards and
            before long, Chang had a cult following.'''},
        {'genre': 'business',
         'label': 'Mill Town: Reckoning with What Remains',
         'author': 'Kerri Arsenault',
         'description': '''
            Kerri Arsenault grew up in the rural
            working class town of Mexico, Maine.
            For over 100 years the community orbited
            around a paper mill that employs most townspeople,
            including three generations of Arsenault’s own family.
            Years after she moved away, Arsenault realized the
            price she paid for her seemingly secure childhood.
            The mill, while providing livelihoods for nearly
            everyone, also contributed to the destruction of
            the environment and the decline of the town’s
            economic, physical, and emotional health in a
            slow-moving catastrophe, earning the area the
            nickname “Cancer Valley. ”Mill Town is an
            personal investigation, where Arsenault
            sifts through historical archives and
            scientific reports, talks to family and
            neighbors, and examines her own childhood
            to illuminate the rise and collapse of
            the working-class, the hazards of loving
            and leaving home, and the ambiguous nature
            of toxics and disease. Mill Town is a moral
            wake-up call that asks, Whose lives are we
            willing to sacrifice for our own survival?'''},
        {'genre': 'business',
         'label': '2030: How Today\'s Biggest Trends Will '
         'Collide and Reshape the Future of Everything',
         'author': 'Mauro F.Guillén',
         'description': '''
            The world is changing drastically
            before our eyes—will you be prepared
            for what comes next? A groundbreaking
            analysis from one of the world's foremost
            experts on global trends, including analysis
            on how COVID-19 will amplify and accelerate
            each of these changes. Once upon a time,
            the world was neatly divided into
            prosperous and backward economies.
            Babies were plentiful, workers outnumbered
            retirees, and people aspiring towards the
            middle class yearned to own homes and cars.
            Companies didn't need to see any further
            than Europe and the United States to do well.
            Printed money was legal tender for all debts,
            public and private. We grew up learning how to
            "play the game," and we expected the rules to
            remain the same as we took our first job,
            started a family, saw our children grow up,
            and went into retirement with our
            finances secure.'''},
        {'genre': 'science',
         'label': 'Interference',
         'author': 'Brad Parks',
         'description': '''
            From international bestselling author
            Brad Parks comes an emotional, heart-pounding
            thriller that explores the scientific
            unknown—and one woman’s efforts to save
            her husband from its consequences.
            Quantum physicist Matt Bronik is suffering
            from strange, violent seizures that medical
            science seems powerless to explain—much
            to the consternation of his wife, Brigid.
            Matt doesn’t think these fits could be
            related to his research, which he has
            always described as benign and esoteric.
            That, it turns out, is not quite true:
            Matt has been prodding the mysteries
            of the quantum universe, with terrible
            repercussions for his health.
            And perhaps even for humanity as a whole.'''},
        {'genre': 'science',
         'label': 'Find Layla: A Novel',
         'author': 'Meg Elison',
         'description': '''
            A neglected girl’s chaotic coming-of-age
            becomes a trending new hashtag in a novel
            about growing up and getting away by an
            award-winning author. Underprivileged and
            keenly self-aware, SoCal fourteen-year-old
            Layla Bailey isn’t used to being noticed.
            Except by mean girls who tweet about her
            ragged appearance. All she wants to do is
            indulge in her love of science, protect
            her vulnerable younger brother, and
            steer clear of her unstable mother. Then a
            school competition calls for a biome.
            Layla chooses her own home, a hostile
            ecosystem of indoor fungi and secret shame.
            With a borrowed video camera,
            she captures it all. The mushrooms
            growing in her brother’s dresser.
            The black mold blooming up the apartment walls.
            The unmentionable things living
            in the dead fridge. All the inevitable
            exotic toxins that are Layla’s life.
            Then the video goes viral.'''},
        {'genre': 'science',
         'label': 'The Overstory',
         'author': 'Richard Powers',
         'description': '''
            The Overstory is a sweeping,
            impassioned work of activism and
            resistance that is also a stunning
            evocation of - and paean to -
            the natural world. From the roots
            to the crown and back to the seeds,
            Richard Powers’s twelfth novel unfolds
            in concentric rings of interlocking
            fables that range from antebellum New York
            to the late twentieth-century Timber Wars
            of the Pacific Northwest and beyond.
            There is a world alongside ours—vast,
            slow, interconnected, resourceful,
            magnificently inventive, and almost
            invisible to us. This is the story of a
            handful of people who learn how to see
            that world and who are drawn up into
            its unfolding catastrophe.'''},

    ]
    return render_template('book.html', book=book, books=books)


if __name__ == "__main__":
    app.debug = True
    app.run()
