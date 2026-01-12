#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:38:58 2025

@author: alya
"""


TBD = None # Platzhalter


sem1 = {"pro1M" : [[(5.5, 0.1, "Konzeptskizze"), (5.8, 0.15, "Sitzungsprotokolle"), (4.9, 0.2, "Reflexionsbericht"), (5.3, 0.15, "Fertigungszeichnung"), (5, 0.15, "Bericht Teil: Sprachkompetenz"), (4.8, 0.15, "Bericht Teil: Konstruktion"), (5.5, 0.1, "Präsentation")], [None], 6],
        "an1"   : [[4.6, 4.4, (5.1, 1, "Bonus +0.2 Note für Python-Aufgabe Newton-Verfahren")], [4.9], 3],
        "mechM" : [[5, 3.5, 5], [5.2], 3],
        "lalg1" : [[4.2, 4.7], [4.7], 3],
        "esfss" : [[(5.58, 0.6, "Presentation"), (5.35, 0.4, "Final Exam")], [None], 2],
        "AuA"   : [[(5.8, 0.5, "1-Minuten-Rede"), (5.2, 0.2, "Analyse Auftritt"), (4.5, 0.3, "Podium")], [None], 2],
        "infM"  : [[(6.1, 0.5), (5.4, 0.25, "Projekt"), (5.6, 0.25, "Projekt")], [None], 3],
        "werk"  : [[5.4, 4.8], [None], 3],
        "ch1"   : [[4.5], [4.3], 3],
        "hkon"  : [[(4.65, 0.5, "Teil Herstellung"), (6, 0.2, "Teil Konstruktion Peergrading Zeichnung"), (4.6, 0.3, "Teil Konstruktion")], [None], 3]
        }


sem2 = {"pro2M" : [[(5.75, 0.1, "Sitzungsmoderation"), (4.5, 0.15, "Patentrecherche"), (4.8, 0.15, "Technischer Bericht Sprachkompetenz"), (4.9, 0.2, "Zeichnungssatz")], [None], 6],
        "thdM"  : [[4.5], [3.5], 3],
        "an2"   : [[4.9, 4, (5.06, 1, "Bonus +0.2 Note für Python-Aufgabe")], [4.3], 3],
        "lalg2" : [[(5.2, 2), (4.7, 1)], [None], 3],
        "chkL"  : [[(5.1, 0.25, "Chemie Schriftliche Prüfung"), (5.166, 0.125, "Chemiepräsentation"), (4.333, 0.125, "Chemie-Laborbericht"), (5, 0.5, "CADA-Challenge-und-Präsentation")], [None], 3],
        "stk"   : [[5.18, 4.2], [None], 3],
        "wisa"  : [[5], [None], 2],
        "wus"   : [[3.8, 4.8], [4], 3],
        "mel"   : [[(3.45, 1), (3.95, 1), (4.88, 1.25)], [None], 3],
        "eidpe" : [[(6, 0.1, "Moodle Exercises"), (5.5, 0.4, "Poster and Canvas"), (4.5, 0.5, "Pitch")], [None], 2],
        "werk2" : [[3.72], [4.9], 3],
        "ecae"  : [[None], [None], 4] # 4 ECTS angerechnet durch C1 Zertifikat
       }


sem3 = {"pro3M" : [[(5, 1, "Abgabe A"), (5, 1.5, "Abgabe B"), (5.1, 2.5, "Abgabe D (Einzelarbeit)"), (5, 2, "Abgabe E")], [None], 6],
        "lean"  : [[(5.8, 0.4, "Schriftliche Prüfung"), (TBD, 0.6, "Präsentation & Prozessdokumentation")], [None], 2],
        "bplan" : [[(5.8, 0.3, "Schriftliche Prüfung"), (TBD, 0.4, "Businessplan-Reasoning & Anhang"), (TBD, 0.3, "Elevator-Pitch & Q&A")], [None], 2],
        "kmk"   : [[4.8, 3.5], [None], 3],
        "eltM"  : [[(6, 0.15, "Labor 1"), (4.3, 0.7, "Schriftliche Prüfung"), (TBD, 0.15, "Labor 2")], [TBD], 3],
        "elstk" : [[4.2], [TBD], 3],
        "num"   : [[5.5, 3.3], [None], 3],
        "flmM"  : [[3], [TBD], 3]
       }

sem4 = {"pro4M" : [[], [None], 6],
        "md"    : [[], [TBD], 3],
        "fems"  : [[], [None], 3],
        "atL"   : [[], [None], 3],
        "egts"  : [[], [TBD], 3],
        "man"   : [[], [TBD], 3],
        "wst"   : [[], [TBD], 3],
        "ffup"  : [[], [None], 2],
        "ereth" : [[], [None], 2],
        "rukg"  : [[], [None], 2]
       }

sem5 = {"pro5M" : [[], [None], 6]
        # TBD
       }

sem6 = {"pro6Ma": [[], [None], 6]
        # TBD
       }

sem7 = {# TBD
       }




def round_half_up(number, decimals=0):
    multiplier = 10**decimals
    return int(number * multiplier + 0.5) / multiplier


def average(grades, round_average = False):
    if grades == [] or grades == [None] or grades == None:
        return None

    grades_weighted = []
    grades_weights = []
    for grade in grades:
        if grade is None:                 # None Platzhalter überspringen
            continue
        if type(grade) == tuple:
            if grade[0] is None:          # None Platzhalter überspringen
                continue
            grades_weights.append(grade[1])
            grade = grade[0] * grade[1]
        else:
            grades_weights.append(1)
        grades_weighted.append(grade)
    if sum(grades_weights) == 0:          # None Platzhalter überspringen: -> Schutz vor Division durch 0
        return None
    weight_total = sum(grades_weights)
    average = sum(grades_weighted) * 1/weight_total
    if round_average != False:
        return round_half_up(average, round_average)
    return average


def grades(semester):
    modules = list(semester.keys())
    results = {}

    ects_total_positive = 0
    ects_total_negative = 0
    grades_final = []

    for module in modules:
        grades_semester = semester[module][0]
        grades_final_exam = semester[module][1]
        ects_module = semester[module][2]

        average_semester = average(grades_semester, round_average=1)
        average_final_exam = average(grades_final_exam, round_average=1)

        averages = []
        if average_semester != None:
            averages.append(average_semester)
        if average_final_exam != None:
            averages.append(average_final_exam)

        if len(averages) != 0:
            average_total = round_half_up(sum(averages) / len(averages), 1)
            if average_total >= 3.75:
                grades_final.append(average_total)
        else:
            average_total = None

        if average_total:
            if average_total >= 3.75:
                ects_final = ects_module
                ects_total_positive += ects_module
            else:
                ects_final = - ects_module
                ects_total_negative -= ects_module
        else:
            ects_final = ects_module
            ects_total_positive += ects_module

        results[module] = (average_semester, average_final_exam, average_total, ects_final)

    grades_final_average = average(grades_final)
    return results, grades_final_average, (ects_total_positive, ects_total_negative)





def print_table_rich(results, title=None):
    """
    Ausgabe einer formatierten Tabelle.
    Eingabe: grades(grades_dict), title="Titel"
    """
    from rich.table import Table
    from rich.console import Console

    results_dict = results[0]
    grades_final_average = results[1]
    ects_total = results[2]

    # Titel
    console = Console()
    if title != None:
        table = Table(title=title)

    # Spalten definieren
    table.add_column("Modul  ", style="bold", justify="left")
    table.add_column("Erfa ", justify="right")
    table.add_column("MSP  ", justify="right")
    table.add_column("Final", justify="right")
    table.add_column("ECTS",  justify="right")


    # Mit Farben Formatieren
    def format_grade(val):
        if val is None:
            return "-"
        if val < 3.75:
            return f"[red]{val:.1f}[/red]"
        elif val < 4.0:
            return f"[yellow]{val:.1f}[/yellow]"
        else:
            return f"[green]{val:.1f}[/green]"

    def format_ects(val):
        if val is None:
            return "-"
        if val < 0:
            return f"[red]{val}[/red]"
        else:
            return f"[green]{val}[/green]"

    # Tabellieren
    for module, (average_semester, average_final_exam, average_total, ects_final) in results_dict.items():
        table.add_row(
            module,
            format_grade(average_semester),
            format_grade(average_final_exam),
            format_grade(average_total),
            format_ects(ects_final))

    table.add_section()

    table.add_row(
        "Total",
        "",
        "",
        format_grade(grades_final_average),
        f"[green]{ects_total[0]}[/green]")

    table.add_row(
        "",
        "",
        "",
        "",
        f"[red]{ects_total[1]}[/red]")

    # Ausgabe Tabelle in Konsole
    print("")
    console.print(table)




# Abruf Tabellen
print_table_rich(grades(sem1), "Sem. 1")
print_table_rich(grades(sem2), "Sem. 2")
print_table_rich(grades(sem3), "Sem. 3")
print_table_rich(grades(sem4), "Sem. 4")
"""
print_table_rich(grades(sem5), "Sem. 5")
print_table_rich(grades(sem6), "Sem. 6")
print_table_rich(grades(sem7), "Sem. 7")
"""




# input("\n\nPress Enter to quit...\n")
