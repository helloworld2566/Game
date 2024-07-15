label ep2:
    scene 41i
    play sound "door_open.mp3" noloop
    pause
    scene 42i
    "As I got ready for school, I see my [m] in the hallway and decide to talk to her before leaving to school."
    scene 43i
    y "[m] I'm leaving for school!"
    y "Okay honey. Have a good day."

    if peek:
        menu:
            "Apologise for yesterday":
                scene 42
                "I need to talk to [m], apologize for my actions, and figure out a way to confront my feelings without causing any further discomfort or awkwardness for either of us."
                "I take a deep breath and muster up the courage to face my [m]."
                y "[m], can we talk for a minute? I want to say I'm sorry for what happened yesterday."
                "[m], sensing the gravity of the situation, looks at me with concern."
                m "Of course, sweetheart. What's on your mind?"
                y "First of all, I need to apologize for walking in on you earlier."
                y "I know it was inappropriate, and I'm really sorry for making you uncomfortable. I never want to put you in an awkward position like that again."
                scene 43
                m "Thank you for your apology, sweetheart."
                m "I appreciate it. I know you didn't mean any harm, and these things happen sometimes."

                menu:
                    "Talk about your urges":
                        y "What if [m] becomes disappointed in me, or worse, disgusted?"
                        y "I have to be ready to face whatever reaction she may have."
                        y "{i}She loves me no matter what. I need to trust that she'll try to understand and help.{/i}"
                        y "But there's something else I need to discuss. I feel weird, and I don't understand why I'm having these thoughts about you. And, honestly, it scares me."
                        scene 44
                        m "I'm here for you, sweetheart. It's important that we can talk about these feelings openly and honestly."
                        m "Is this something you've been struggling with for a while?"
                        scene 45
                        y "Yeah, I think it started around puberty, but it's been getting more intense lately."
                        y "I don't want to feel this way, and I've been trying to push these thoughts aside,"
                        y "but I know I cannot keep avoiding them."
                        m "Honey these things are common for boys your age."
                        scene 46
                        y "Really, [m]? You think it's normal for me to have these thoughts and feelings?"
                        scene 47
                        m "Yes, sweetheart. It's not uncommon for boys your age to experience sexual feelings, even towards those close to them."
                        m "But it's essential to understand that acting on these feelings is not appropriate."
                        m "And with time and maturity, these feelings will often subside and evolve."
                        scene 48
                        y "But why do I keep having these thoughts about you, even though I know it's wrong?"
                        y "It's confusing and disturbing."
                        m "It's essential to explore why you might be having these thoughts."
                        m "It could be due to a variety of factors, such as curiosity, hormonal changes, or even challenging life situations."
                        m "It's also important to learn how to manage these feelings in a healthy way."
                        m "This is where talking to a therapist could truly help you."
                        "As I speak my deepest fears aloud, I feel a weight lifting off my shoulders, allowing the healing process to begin."
                        y "What do you think I should do next? I don't want to cause any more pain or discomfort for either of us."
                        scene 49
                        m "I think it's important for you to talk to a professional therapist, sweetheart."
                        m "They can help you navigate these complex emotions and find ways to move past them."
                        m "In the meantime, I want to assure you that our relationship remains a safe and supportive space, free from judgment."
                        y "Thank you, [m]. I really appreciate your support."
                        y "I'll start looking for a therapist who can help me understand and manage these feelings."
                        scene 50
                        m "You're a strong, brave per[s], sweetheart."
                        m "You'll get through this, and I'll be here for you every step of the way."

                        "I leave our conversation with a newfound sense of hope and determination."
                        "With my [m]'s support and the guidance of a mental health professional, I will confront and overcome my unresolved emotions and inappropriate thoughts."
                
                    "Don't talk about your urges":
                        y "{i}I can't bring myself to talk about my feelings with [m].{/i}"
                        y "{i}I'm really late I should hurry up.{/i}"
                
            "Don't Apolosise":
                scene 43i
                y "{i}I'm really late I should hurry."

    "I leave for school, my mind still consumed by the events of the morning."
    jump ep3