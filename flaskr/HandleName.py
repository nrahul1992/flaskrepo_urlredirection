from random import randint


def hellothere( name):
    quotes = ["'If people do not believe that mathematics is simple, it is only because "
              "they do not realize how complicated life is.' -- John Louis von Neumann ",
               "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
               "'To understand recursion you must first understand recursion..' -- Unknown",
               "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
               "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
               "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomnumber = randint(0, len(quotes)-1)
    name = name + "\t see this also works"
    vals = {"quote": quotes[randomnumber],
            "xyz": name}

    #   return render_template('test.html', name=name)
    #   return render_template('test.html', **locals())
    return vals


#   obj = Test1().hello()


