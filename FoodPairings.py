"""
foodPairings = {
    'meat': '7155+3008',
    'cheese': '7155+3009',
    'dessert': '7155+3010',
    'pasta&grains': '7155+3012',
    'poultry': '7155+3013',
    'seafood': '7155+3014',
    'meat+beef': '7155+3015',
    'meat+lamb': '7155+3016',
    'meat+pork': '7155+3017',
    'meat+veal': '7155+3018',
    'meat+beef+herbs': '7155+3019',
    'meat+beef+hot spices': '7155+3020',
    'meat+beef+mushroom': '7155+3021',
    'meat+beef+stew': '7155+3022',
    'meat+beef+bbq': '7155+3023',
    'meat+beef+burgers': '7155+3024',
    'meat+lamb+herbs': '7155+3025',
    'meat+lamb+hot spices': '7155+3026',
    'meat+pork+herbs': '7155+3027',
    'meat+pork+hot spices': '7155+3028',
    'meat+pork+mushroom': '7155+3029',
    'meat+pork+sausage': '7155+3030',
    'meat+pork+tenderloin': '7155+3031',
    'meat+pork+bbq': '7155+3032',
    'meat+pork+breaded': '7155+3033',
    'meat+pork+fruit': '7155+3034',
    'meat+veal+herbs': '7155+3035',
    'meat+veal+lemon/citrus': '7155+3036',
    'meat+veal+mushroom': '7155+3037',
    'meat+veal+breaded': '7155+3038',
    'meat+veal+chops': '7155+3039',
    'cheese+blue': '7155+3040',
    'cheese+cheddar': '7155+3041',
    'cheese+creamy': '7155+3042',
    'cheese+goat': '7155+3043',
    'cheese+hard': '7155+3044',
    'cheese+semi-firm': '7155+3045',
    'cheese+stinky': '7155+3046',
    'dessert+berries': '7155+3047',
    'dessert+chocolate': '7155+3048',
    'dessert+cream or custard': '7155+3049',
    'dessert+lemon': '7155+3050',
    'pasta&grains+lasagne': '7155+3055',
    'pasta&grains+paella': '7155+3056',
    'pasta&grains+pasta': '7155+3057',
    'pasta&grains+pizza': '7155+3058',
    'pasta&grains+risotto': '7155+3059',
    'pasta&grains+lasagne+meat': '7155+3060',
    'pasta&grains+lasagne+vegetable': '7155+3061',
    'pasta&grains+pizza+meat': '7155+3062',
    'pasta&grains+pizza+vegetable': '7155+3063',
    'pasta&grains+risotto+mushroom': '7155+3064',
    'pasta&grains+risotto+plain': '7155+3065',
    'pasta&grains+risotto+primavera': '7155+3066',
    'pasta&grains+pasta+meat': '7155+3067',
    'pasta&grains+pasta+mushroom': '7155+3068',
    'pasta&grains+pasta+pesto': '7155+3069',
    'pasta&grains+pasta+tomato-base': '7155+3070',
    'pasta&grains+pasta+vegetable': '7155+3071',
    'pasta&grains+pasta+white sause': '7155+3072',
    'pasta&grains+pasta+cream-based': '7155+3073',
    'poultry+cassoulet': '7155+3074',
    'poultry+chicken': '7155+3075',
    'poultry+duck': '7155+3076',
    'poultry+turkey': '7155+3077',
    'poultry+chicken+herbs': '7155+3078',
    'poultry+chicken+lemon/citrus': '7155+3079',
    'poultry+chicken+mushroom': '7155+3080',
    'poultry+chicken+mustard': '7155+3081',
    'poultry+chicken+spicy': '7155+3082',
    'poultry+chicken+bbq': '7155+3083',
    'poultry+chicken+cream-based': '7155+3084',
    'poultry+chicken+fried': '7155+3085',
    'poultry+duck+seared': '7155+3086',
    'poultry+duck+confit': '7155+3087',
    'poultry+duck+fois gras': '7155+3088',
    'poultry+duck+fruit': '7155+3089',
    'poultry+turkey+lemon': '7155+3090',
    'poultry+turkey+roasted': '7155+3091',
    'poultry+turkey+breaded': '7155+3092',
    'seafood+crab': '7155+3093',
    'seafood+lobster': '7155+3094',
    'seafood+oysters': '7155+3095',
    'seafood+salmon': '7155+3096',
    'seafood+scallops': '7155+3097',
    'seafood+shrimp': '7155+3098',
    'seafood+sushi': '7155+3099',
    'seafood+tuna': '7155+3100',
    'seafood+white fish': '7155+3101',
    'seafood+crab+soft shelled': '7155+3102',
    'seafood+crab+spicy': '7155+3103',
    'seafood+crab+butter': '7155+3104',
    'seafood+crab+crab cakes': '7155+3105',
    'seafood+lobster+butter': '7155+3106',
    'seafood+salmon+herbs': '7155+3107',
    'seafood+salmon+mustard': '7155+3108',
    'seafood+salmon+grilled': '7155+3109',
    'seafood+scallops+herbs': '7155+3110',
    'seafood+scallops+lemon/citrus': '7155+3111',
    'seafood+scallops+butter': '7155+3112',
    'seafood+shrimp+lemon/citrus': '7155+3113',
    'seafood+shrimp+herbs': '7155+3114',
    'seafood+tuna+seared': '7155+3115',
    'seafood+tuna+spicy': '7155+3116',
    'seafood+white fish+herbs': '7155+3117',
    'seafood+white fish+hot spices': '7155+3118',
    'seafood+white fish+lemon/citrus': '7155+3119',
    'seafood+white fish+stew': '7155+3120',
    'seafood+white fish+fish tacos': '7155+3121',
    'seafood+white fish+fried': '7155+3122'
    
}
"""

"""
General format:
   For a given food:
        'food': {
            'id': '<the_category_id>',
            'question': <the_question_for_refining_search>,
            'categories': {
                # more foods
            }
        }

foodPairings = {
    'id': None
    'question': <the_first_question>
    'categories':  {
        # begin listing foods
    }
}

If no question is present, then no more categories to loop over.

"""

# Note: When using food pairings, make sure to add into the category a
# 7155+<category_id>
# i.e., the category for meat is 7155+3008

foodPairings = {
    'id': None,
    'question': 'Do you plan on having a meal with the wine?  If so, what category does it fall under?: Meat, cheese, dessert, pasta and grains, poultry, seafood, or none of these.',
    'question': 'Do you plan on having a meal with the wine?  For example, will you have meat, cheese, dessert, pasta and grains, poultry, seafood, or none of these?',
    'categories': {
        'meat': {
            'id': '3008',
            'question': 'Will it be beef, lamb, pork, veal, or none of these?',
            'categories': {
                'beef': {
                    'id': '3015',
                    'blurb': 'Beef has lots of protein and some fat as well, which need wine with good structure and tannin, such as Cabernet Sauvignon, Merlot, Bordeaux blends, Nebbiolo, Malbec or Petite Sirah',
                    'question': 'How will you be preparing the beef?  Will it be with herbs, hot spices, mushroom, as a stew, barbeque, burgers, or none of these?',
                    'categories': {
                        'herbs': {
                            'id': '3019',
                            'blurb': 'For beef with herbs, try a wine that has herbal notes to compliment the food, and good tannins to balance the fat and protein in the meat. Syrah from the Rhone Valley or Washington State, Malbec, Ribera del Duero or a good Chilean red will pair well.'
                        },
                        'hot spices': {
                            'id': '3020',
                            'blurb': 'Hot spices need sweet fruit, but the meat still needs some good structure. Try Zinfandel, California Syrah or a Malbec'
                        },
                        'mushroom': {
                            'id': '3021',
                            'blurb': 'Mushroom sauces give an earthy quality to the meal, so try a more rustic red such as Rhone Syrah, Bordeaux, a Burgundian Pinot Noir or a Ribera del Duero.'
                        },
                        'stew': {
                            'id': '3022',
                            'blurb': 'Beef stew is a comfort food and needs a comfort wine. Choose from red Bordeaux blends, Rioja, Piedmont reds (such as Barolo or Barbaresco) or Tuscan reds'
                        },
                        'barbeque': {
                            'id': '3023',
                            'blurb': 'BBQ sauce has a sweet and spicy component that marries well with a structured wine with concentrated fruit. Try Zinfandel, Malbec, Australian Reds, Mourvedre/Monastrell or Petite Sirah.'
                        },
                        'burgers': {
                            'id': '3024',
                            'blurb': 'A juicy burger wants a juicy wine, but with a bit of backbone. Try cru Beaujolais, Rhone red blends, South African reds or Australian Shiraz'
                        }
                    }
                },
                'lamb': {
                    'id': '3016',
                    'blurb': 'A gamey meat, lamb pairs well with wine that has herbal or gamey notes. Try red wines from the Rhone, like Chateauneuf-du-Pape, and Pinotage or Bordeaux',
                    'question': 'Will you be putting herbs, hot spices, or none of these on the lamb?',
                    'categories': {
                        'herbs': {
                            'id': '3025',
                            'blurb': 'Lamb with herbs is a classic match for Chateauneuf-du-Pape and other Rhone reds such as Gigondas and Vacqueras. Also try a Northern Rhone red like Hermitage or Cornas'
                        },
                        'hot spices': {
                            'id': '3026',
                            'blurb': 'Hot spices need sweet fruit, but this gamey meat also needs some structure. Try South American Syrah or Cabernet Sauvignon or South African reds.'
                        }
                    }
                },
                'pork': {
                    'id': '3017',
                    'blurb': 'Pork, the "other" white meat, is generally mild when served plain. Classic pairings include Pinot Noir, Cotes-du-Rhone and Tempranillo - all have a healthy balance of fresh fruit and acidity.',
                    'question': 'What do you plan on doing with the pork?  Do you want to add herbs, hot spices, mushrooom, or fruit?  Or instead will you have it as sausage, tenderloin, barbeque, breaded, or none of these?',
                    'categories': {
                        'herbs': {
                            'id': '3027',
                            'blurb': 'The other white meat mixed with herbs requires something with an herbal kick, but not too heavy. Rhone red blends, Rioja and Carmenere will offer just that.'
                        },
                        'hot spices': {
                            'id': '3028',
                            'blurb': 'Hot spices need sweet fruit, but pork is a lighter meat, so avoid wines that are too heavy. Australian reds from cool climates, like the Yarra Valley, work well, as do lighter Zinfandels or Mourvedre.'
                        },
                        'mushroom': {
                            'id': '3029',
                            'blurb': 'Pork and mushrooms are a great flavor match. They call for a medium-bodied red with good fruit and mild tannins,  like a New Zealand or Oregon Pinot Noir or a Merlot-based Bordeaux.'
                        },
                        'sausage': {
                            'id': '3030',
                            'blurb': 'The spice in sausage goes well with wines that have some big fruit, a touch of spice, and not too many tannins. Try Cotes-du-Rhone, Grenache or a dry Rose.'
                        },
                        'tenderloin': {
                            'id': '3031',
                            'blurb': 'A very tender cut of meat, the pork tenderloin goes well with a good balance of flavors and structure. Try Pinot Noir, Ribera del Duero or Merlot (Washington State Merlots are particularly delicious).'
                        },
                        'barbeque': {
                            'id': '3032',
                            'blurb': 'Ribs or roast, pork with BBQ sauce needs some red with fruit and spice, but medium tannins. Try Zinfandel, Cotes-du-Rhone, Australian reds or Argentina Malbec.'
                        },
                        'breaded': {
                            'id': '3033',
                            'blurb': 'Breaded pork goes well with both red and white wines. For whites try an Italian white, like Falenghina or Arneis. Viognier is another great match. For reds go with a Tuscan red or Tempranillo.'
                        },
                        'fruit': {
                            'id': '3034',
                            'blurb': 'Pork with a fruit sauce likes fruit-forward wines. If the fruit on your meat is red (like cherry), match with Pinot Noir (particularly California). White fruits sauces (like peach or apple) go well with Torrontes, Spanish whites or even Viognier.'
                        }
                    }
                },
                'veal': {
                    'id': '3018',
                    'blurb': 'Veal is a delicate meat, but with distinct flavors. Try a rose (particularly of the sparkling kind),a Viognier or white Bordeaux if you\'re up for white. For reds, a Merlot or Pinot Noir will pair nicely.',
                    'question': 'Several ways of preparing pork would be with herbs, lemon / citrus, mushroom, breaded, and in chops.  Which one do you plan on doing?',
                    'categories': {
                        'herbs': {
                            'id': '3035',
                            'blurb': 'An herb rub on veal calls for a fruit-forward red like Merlot or Pinot Noir'
                        },
                        'lemon': {
                            'id': '3036',
                            'blurb': 'Lemon and citrus sauces on mild meat, like veal, call for bright whites with good acidity. Try an Italian white wine or a bright Rose.'
                        },
                        'citrus': {
                            'id': '3036',
                            'blurb': 'Lemon and citrus sauces on mild meat, like veal, call for bright whites with good acidity. Try an Italian white wine or a bright Rose.'
                        },
                        'lemon or citrus': {
                            'id': '3036',
                            'blurb': 'Lemon and citrus sauces on mild meat, like veal, call for bright whites with good acidity. Try an Italian white wine or a bright Rose.'
                        },
                        'mushroom': {
                            'id': '3037',
                            'blurb': 'The earthy mushroom flavor on this delicate meat will go well with a good Pinot Noir (particularly from Oregon, France or New Zealand) or a Merlot'
                        },
                        'breaded': {
                            'id': '3038',
                            'blurb': 'Breaded veal ads a richer flavor to the delicate meat - try an old-world wine - a red or white Burgundy would be perfect, or a rustic Tuscan red, like Chianti.'
                        },
                        'chops': {
                            'id': '3039',
                            'blurb': 'Veal chops are simple, but rich. Try either a fresh rose or Viognier'
                        }
                    }
                }
            }
        },
        'cheese': {
            'id': '3009',
            'question': 'What kind of cheese do you have in mind?  There\'s blue, cheddar, creamy, goat, hard, semi-firm, stinky, and of course none of these.',
            'categories': {
                'blue': {
                    'id': '3040',
                    'blurb': 'Blue cheese goes best with wines low in tannins and high in sugar. Try Port, Sauternes or an Australian Muscat'
                },
                'cheddar': {
                    'id': '3041',
                    'blurb': 'Cheddar\'s sharp bite needs carbonation & acid - sparkling wine is the best match here'
                },
                'creamy': {
                    'id': '3042',
                    'blurb': 'The acidity and carbonation of sparkling wine cuts through the creamy cheese, giving an excellent contrast of texture. Other good matches are Chablis or White Burgundy.'
                },
                'goat': {
                    'id': '3043',
                    'blurb': 'The sharpness of goat cheese is well-matched with a bright, acidic white. Try Sauvignon Blanc, Sparkling wine or a Chablis'
                },
                'hard': {
                    'id': '3044',
                    'blurb': 'Hard cheeses can stand up well to reds, but the red should have a good fruit component. Try a fruity Pinot Noir, Zinfandel, Merlot or a raisin-y Amarone'
                },
                'semi-firm': {
                    'id': '3045',
                    'blurb': 'Semi-firm cheeses, particularly sheep\'s cheese, are good matchs with many wines, especially those from the same regions (think Pyranees). Try with Italian reds, Spanish reds or a Rhone red.'
                },
                'stinky': {
                    'id': '3046',
                    'blurb': 'Rich, stinky cheese can make some wines taste bad. Enjoy with an aromatic, slightly sweet wine such as Gewurztraminer, Riesling, or a Pinot Gris from Alsace.'
                }
            }
        },
        'dessert': {
            'id': '3010',
            'question': 'Will you be having berries, chocolate, cream / custard, lemon, or none of these for dessert?',
            'categories': {
                'berries': {
                    'id': '3047',
                    'blurb': 'Berry fruit desserts are great with good flavor and acid, like Beaumes de Venise, Ice Wine, Vin Santo or even Australian Muscat'
                },
                'chocolate': {
                    'id': '3048',
                    'blurb': 'Chocolate desserts vary according to how much chocolate and what percent cocoa is involved. While Port is a classic, dark chocolate pairs well with still red wines, like fruit-forward Pinot Noir and Australian Shiraz. For sweeter chocolate, try a Banyuls or an Australian Muscat, or "sticky."'
                },
                'cream': {
                    'id': '3049',
                    'blurb': 'A cream or custard pairs well with lighter dessert wines with good acidity, like Sauternes, Beaumes-de-Venise, ice wine or Muscat'
                },
                'custard': {
                    'id': '3049',
                    'blurb': 'A cream or custard pairs well with lighter dessert wines with good acidity, like Sauternes, Beaumes-de-Venise, ice wine or Muscat'
                },
                'cream or custard': {
                    'id': '3049',
                    'blurb': 'A cream or custard pairs well with lighter dessert wines with good acidity, like Sauternes, Beaumes-de-Venise, ice wine or Muscat'
                },
                'lemon': {
                    'id': '3050',
                    'blurb': 'A lemon based dessert needs lighter dessert wines with good acidity, like Sauternes, Beaumes-de-Venise, Moscato d\'Asti or an Auslese Riesling'
                }
            }
        },
        'pasta and grains': {
            'id': '3012',
            'question': 'Several kinds of pasta / grains I am familiar with include lasagne, paella, actual pasta, pizza, and risotto.  Let me know which one you plan on having, or tell me that it is none of these if so.',
            'categories': {
                'lasagne': {
                    'id': '3055',
                    'question': 'What kind of lasagne do you plan on having?  Will it be meat, vegetable, or none of these?',
                    'categories': {
                        'meat': {
                            'id': '3060',
                            'blurb': 'Lasagne has a myriad of flavors. With the meat and tomato sauce, try Italian reds like Chianti, Barbera and Southern Italian Reds'
                        },
                        'vegetable': {
                            'id': '3061',
                            'blurb': 'Lasagne has a myriad of flavors. For vegetable lasagne, look for wines with a good acid/fruit balance such as Barbera, Italian or Spanish whites and California Sauvignon Blanc'
                        }
                    }
                },
                'paella': {
                    'id': '3056',
                    'blurb': 'A mix of shellfish and/or meats with the spicy rice of Paella match well with Spanish whites (like Albarino or Rueda), Rose, Rioja, Grenache or Pinot Gris'
                },
                'pasta': {
                    'id': '3057',
                    'blurb': 'Pasta, a fairly bland food, is enhanced with butter or olive oil. Try a mild white, like Italian white, Spanich white or a White Rhone Blend',
                    'question': 'There are a lot of choices for pasta.  They include meat, mushroom, pesto, tomato-base, vegetable, white sauce, and cream-based.  Let me know which one, or tell me that it is none of them if so.',
                    'categories': {
                        'meat': {
                            'id': '3067',
                            'blurb': 'Pair your pasta and meat sauce with a red that is sturdy, but contains good acidity. Try Italian reds like Barbera, Chianti, Brunello di Montalcino and Aglianico'
                        },
                        'mushroom': {
                            'id': '3068',
                            'blurb': 'Mushrooms have an earthy quality and when mixed with pasta, pair well with Pinot Noir, Barbera or Tempranillo'
                        },
                        'pesto': {
                            'id': '3069',
                            'blurb': 'Garlic and herb-based pesto has a kick, and is a nice match with Italian whites, Pinot Grigio/Pinot Gris or a White Rhone blend'
                        },
                        'tomato-base': {
                            'id': '3070',
                            'blurb': 'The acid from tomatoes pair well with more acidic red wines, particularly from Italy, like Barbera, Dolcetto or Chianti'
                        },
                        'vegetable': {
                            'id': '3071',
                            'blurb': 'Vegetables with pasta vary, so try a versatile wine with good acidity such as Italian or Spanish whites, Gruner Veltliner, Pinot Blanc or a dry Rose'
                        },
                        'white sauce': {
                            'id': '3072',
                            'blurb': 'Seafood and white sauces go well with crisp Chardonnay (such as Chablis), aromatic Spanish whites or White Rhone Blends. Also try Sparkling wine, which is a great match!'
                        },
                        'cream-based': {
                            'id': '3073',
                            'blurb': 'You can complement the dish with a creamy white, such as Chardonnay or Viognier, or contrast it with a crisp white, like Italian whites or anything sparkling, like Cava or Prosecco.'
                        }
                    }
                },
                'pizza': {
                    'id': '3058',
                    'question': 'Will the pizza\'s main ingredient be meat, vegetable, or none of these?',
                    'categories': {
                        'meat': {
                            'id': '3062',
                            'blurb': 'Spicy meat and tomato sauce match well with acidic reds like Barbera, Dolcetto or Chianti. A spicy Shiraz also pairs well'
                        },
                        'vegetable': {
                            'id': '3063',
                            'blurb': 'Cheese and vegetables need good fruit in a wine, so try Pinot Gris, Rose, Beaujolais or Shiraz'
                        }
                    }
                },
                'risotto': {
                    'id': '3059',
                    'question': 'Any specific kind of risotto in mind?  There is mushroom, plain, and primavera.',
                    'categories': {
                        'mushroom': {
                            'id': '3064',
                            'blurb': 'For the earthy mushroom flavors and richness of risotto, look for Pinot Noir, Tempranillo or Barbera'
                        },
                        'plain': {
                            'id': '3065',
                            'blurb': 'The simple but rich flavors of risotto do well with Pinot Grigio, Italian Whites, Gruner Veltliner or a White Rhone blend'
                        },
                        'primavera': {
                            'id': '3066',
                            'blurb': 'For paring with vegetables and rich risotto flavors, look for acid and fruit balance with White Rhone blends, Italian or Spanish Whites, or California Sauvignon Blanc'
                        }
                    }
                }
            }
        },
        'poultry': {
            'id': '3013',
            'question': 'Will it be cassoulet, chicken, duck, turkey, or none of these?',
            'categories': {
                'cassoulet': {
                    'id': '3074',
                    'blurb': 'Cassoulet has a myriad of meaty flavors and is a rich, heavy dish. Try a Syrah from Washington or France, a Southern Rhone red, a Southern Italian red or a Bordeaux'
                },
                'chicken': {
                    'id': '3075',
                    'blurb': 'Chicken is a mild meat and served plain, could match with just about anything, as it won\'t overpower the wine. It does particularly well with Chardonnay, Italian whites or White Rhone Blends',
                    'question': 'There are many ways of preparing chicken, several which includes with herbs, lemon / citrus, mushroom, mustard, spicy, as a barbeque, cream-based, and of course fried.  Which one is it?',
                    'categories': {
                        'herbs': {
                            'id': '3078',
                            'blurb': 'Mild chicken flavors and herbs go well wth good acid and light fruit. Pair with Italian whites, White Rhone Blends, Gruner Veltliner or Chenin Blanc. For reds, try a red Rhone blend'
                        },
                        'lemon': {
                            'id': '3079',
                            'blurb': 'A lemon/citrus based sauce and chicken matches well with acidic wines like Sauvignon Blanc, White Rhone blends, Pinot Grigio, Chablis or Chenin Blanc'
                        },
                        'citrus': {
                            'id': '3079',
                            'blurb': 'A lemon/citrus based sauce and chicken matches well with acidic wines like Sauvignon Blanc, White Rhone blends, Pinot Grigio, Chablis or Chenin Blanc'
                        },
                        'lemon or citrus': {
                            'id': '3079',
                            'blurb': 'A lemon/citrus based sauce and chicken matches well with acidic wines like Sauvignon Blanc, White Rhone blends, Pinot Grigio, Chablis or Chenin Blanc'
                        },
                        'mushroom': {
                            'id': '3080',
                            'blurb': 'Earthy mushrooms and mild chicken go well with a Pinot Noir, particularly from New Zealand, Oregon or France.'
                        },
                        'mustard': {
                            'id': '3081',
                            'blurb': 'Spicy mustard with chicken pairs well with the creamy texture of Chardonnay or the fruity components of Beaujolias'
                        },
                        'spicy': {
                            'id': '3082',
                            'blurb': 'Spicy chicken matches well with ripe fruits in wines like Rose, Riesling, Gewurtztraminer, Beaujolais or Viognier'
                        },
                        'barbeque': {
                            'id': '3083',
                            'blurb': 'Spicy and sweet BBQ is a great match with fruit-forward Pinot Noir, Beaujolais or Rose'
                        },
                        'cream-based': {
                            'id': '3084',
                            'blurb': 'Cream-based sauces pair well with creamy wines, like Chardonnay or a Viognier. To contrast the flavors, try a crisp sparkling wine'
                        },
                        'fried': {
                            'id': '3085',
                            'blurb': 'Fried chicken is a heavier preparation, so it needs wine with a bit of weight, like Pinot Gris, Chardonnay from Oregon or California, off-dry Riesling from Washington or Germany, or Rose'
                        }
                    }
                },
                'duck': {
                    'id': '3076',
                    'blurb': 'Pinot Noir is a classic match with a simple duck dish',
                    'question': 'Will the duck be seared, confit, fois gras, with fruit, or none of these?',
                    'categories': {
                        'seared': {
                            'id': '3086',
                            'blurb': 'Pinot Noir is a classic match with a simple duck dish'
                        },
                        'confit': {
                            'id': '3087',
                            'blurb': 'Duck confit is a rich dish that will go well with Spanish reds like Priorat or an earthy Pinot Noir'
                        },
                        'fois gras': {
                            'id': '3088',
                            'blurb': 'The fat content of fois gras is a classic match for the delicate sweetness and bright acidity of a Sauternes. Ice wine is another good match'
                        },
                        'fruit': {
                            'id': '3089',
                            'blurb': 'Fruit-based duck dishes are great with earthy yet fruit-forward wines, like Pinot Noir (particularly a Burgundy) or a modern-style Rioja'
                        }
                    }
                },
                'turkey': {
                    'id': '3077',
                    'blurb': 'Roasted turkey is a bit heavier than other turkeys. Try an aromatic, fruit-forward white like Riesling or a juicy Syrah from Washignton State or California',
                    'question': 'For preparing the turkey, will it be with lemon, roasted, breaded, or none of these?',
                    'categories': {
                        'lemon': {
                            'id': '3090',
                            'blurb': 'A lemon/citrus based turkey dish is great with an acidic, slightly nutty Italian white or a Chenin Blanc'
                        },
                        'roasted': {
                            'id': '3091',
                            'blurb': 'Roasted turkey is typically heavier than other turkey preparations. Try an aromatic, fruit-forward white like Riesling or Gewurztraminer, or a juicy red like Beaujolais, California Pinot Noir or even Zinfandel.'
                        },
                        'breaded': {
                            'id': '3092',
                            'blurb': 'Breaded turkey is a bit heavier in prep method, so try a Riesling or a Semillon'
                        }
                    }
                }
            }
        },
        'seafood': {
            'id': '3014',
            'question': 'Is it crab, lobster, oysters, salmon, scallops, shrimp, sushi, tuna, white fish, or none of these?  If it is multiple, let me know which one will mainly make up the meal.',
            'categories': {
                'crab': {
                    'id': '3093',
                    'question': 'How will you be having the crab?  Will it be soft shelled, spicy, with butter, crab cakes, or none of these?',
                    'categories': {
                        'soft shelled': {
                            'id': '3102',
                            'blurb': 'Soft shelled crabs are a great match for Rose, White Rhone blends and Chenin Blanc, particularly from the Loire'
                        },
                        'spicy': {
                            'id': '3103',
                            'blurb': 'For spicy crab meat, look for something crisp with a touch of sweetness, like Riesling. Also try Rose or an aromatic Spanish white'
                        },
                        'butter': {
                            'id': '3104',
                            'blurb': 'Rich crab with butter are a great match for Chardonnay or Viognier. Also try a White Rhone blend.'
                        },
                        'crab cakes': {
                            'id': '3105',
                            'blurb': 'Crab cakes are slightly rich, so pair a textured wine with them like Viognier, Pinot Gris, Chardonnay or Gruner Veltliner'
                        }
                    }
                },
                'lobster': {
                    'id': '3094',
                    'question': 'Do you plan on having the lobster with butter?',
                    'categories': {
                        'butter': {
                            'id': '3106',
                            'blurb': 'Lobster and butter are great match with a classic Chardonnay'
                        }
                    }
                },
                'oysters': {
                    'id': '3095',
                    'blurb': 'Oysters are salty and briny and need a crisp, mineral-driven wine like Chablis, Muscadet or another Loire white wine'
                },
                'salmon': {
                    'id': '3096',
                    'question': 'Several ways of preparing salmon include with herbs, with mustard, and grilled.  Let me know which one, if any.',
                    'categories': {
                        'herbs': {
                            'id': '3107',
                            'blurb': 'Herbs on Salmon call for a Pinot Noir, Pinot Gris or a crisp Chardonnay'
                        },
                        'mustard': {
                            'id': '3108',
                            'blurb': 'Match the weight of salmon and the spice of mustard with a bright Pinot Noir, Pinot Gris or a Cru Beaujolais'
                        },
                        'grilled': {
                            'id': '3109',
                            'blurb': 'Salmon on the grill brings out the quality flavors of the fish. Pair with Pinot Gris, Chardonnay or Pinot Noir'
                        }
                    }
                },
                'scallops': {
                    'id': '3097',
                    'question': 'How will you prepare the scallops?  Will it be with herbs, lemon / citrus, butter, or none of these?',
                    'categories': {
                        'herbs': {
                            'id': '3110',
                            'blurb': 'Richer scallops with herbs go well with aromatic whites like Torrontes, Albarino and White Rhone blends'
                        },
                        'lemon': {
                            'id': '3111',
                            'blurb': 'Scallops with lemon/citrus need a crisp white. Try Chablis, White Burgundy or Muscadet'
                        },
                        'citrus': {
                            'id': '3111',
                            'blurb': 'Scallops with lemon/citrus need a crisp white. Try Chablis, White Burgundy or Muscadet'
                        },
                        'lemon or citrus': {
                            'id': '3111',
                            'blurb': 'Scallops with lemon/citrus need a crisp white. Try Chablis, White Burgundy or Muscadet'
                        },
                        'butter': {
                            'id': '3112',
                            'blurb': 'A butter-based sauce with rich scallops go well with a richer wine like Chardonnay, Viognier or Vouvray'
                        }
                    }
                },
                'shrimp': {
                    'id': '3098',
                    'question': 'Do you plan on having the shrimp with lemon / citrus, herbs, or none of these?',
                    'categories': {
                        'lemon': {
                            'id': '3113',
                            'blurb': 'Shrimp with lemon/citrus need a crisp white. Try Chablis, White Burgundy or Muscadet'
                        },
                        'citrus': {
                            'id': '3113',
                            'blurb': 'Shrimp with lemon/citrus need a crisp white. Try Chablis, White Burgundy or Muscadet'
                        },
                        'lemon or citrus': {
                            'id': '3113',
                            'blurb': 'Shrimp with lemon/citrus need a crisp white. Try Chablis, White Burgundy or Muscadet'
                        },
                        'herbs': {
                            'id': '3114',
                            'blurb': 'Shellfish with garlic and herbs goes well with crisp aromatic wines like Spanish whites'
                        }
                    }
                },
                'sushi': {
                    'id': '3099',
                    'blurb': 'Sushi has salty and spicy, so is great with sake, sparkling wine or Pinot Gris'
                },
                'tuna': {
                    'id': '3100',
                    'blurb': 'Seared tuna is a heavier fish and goes well with Pinot Noir or Oregon Pinot Gris',
                    'question': 'Is it going to be seared tuna or spicy tuna?',
                    'categories': {
                        'seared': {
                            'id': '3115',
                            'blurb': 'Seared tuna is a heavier fish and goes well with Pinot Noir or Oregon Pinot Gris'
                        },
                        'spicy': {
                            'id': '3116',
                            'blurb': 'Spicy tuna is a nice match with Pinot Gris from Oregon or Alsace or a Rose'
                        }
                    }
                },
                'white fish': {
                    'id': '3101',
                    'blurb': 'White fish can be delicate, yet meaty. Best to have a good wine with balance and not too many flavors to overwhelm the fish. Try Pinot Blanc, White Rhone blends or Pinot Grigio',
                    'question': 'What will you be doing with the white fish?  Will you add herbs, hot spices, or lemon / citrus to it?  Or instead will you have it as a stew, fish tacos, or fried?',
                    'categories': {
                        'herbs': {
                            'id': '3117',
                            'blurb': 'Delicate white fish with some herbs need a lighter wine, but with fruit to match the herbs. Try Torrontes, Pinot Gris or a White Rhone Blend'
                        },
                        'hot spices': {
                            'id': '3118',
                            'blurb': 'Hot spice with white fish matches well with a hint of sweetness in the wine. Try Gewurtztraminer, Riesling, Alsace Pinot Gris or Rose'
                        },
                        'lemon': {
                            'id': '3119',
                            'blurb': 'White fish is delicate and light and the citrus adds acid, so the wine should have a good amount of acid without overpowering the food. Try Sauvignon Blanc, Pinot Blanc or Chenin Blanc'
                        },
                        'citrus': {
                            'id': '3119',
                            'blurb': 'White fish is delicate and light and the citrus adds acid, so the wine should have a good amount of acid without overpowering the food. Try Sauvignon Blanc, Pinot Blanc or Chenin Blanc'
                        },
                        'lemon or citrus': {
                            'id': '3119',
                            'blurb': 'White fish is delicate and light and the citrus adds acid, so the wine should have a good amount of acid without overpowering the food. Try Sauvignon Blanc, Pinot Blanc or Chenin Blanc'
                        },
                        'stew': {
                            'id': '3120',
                            'blurb': 'Fish stew can have a number of flavors, so try something delicate and crisp, like Chablis or Muscadet. For more fruit, go with Albarino, Rueda or Chenin Blanc'
                        },
                        'fish tacos': {
                            'id': '3121',
                            'blurb': 'Fish tacos, while delicate, also have spice. Try something with ripe fruit and maybe a hint of sweetness like Oregon Pinot Gris, Riesling or Gewurtztraminer'
                        },
                        'fried': {
                            'id': '3122',
                            'blurb': 'The richness of fried fish matches well with a creamy white. Try Chardonnay, Viognier or White Rhone blends.'
                        }
                    }
                }
            }
        }
    }
}