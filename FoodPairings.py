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
            'id': <the_category_id>,
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
    'question': 'What kind of food do you plan on eating?',
    'categories': {
        'meat': {
            'id': '3008',
            'question': 'Any specific kind of meat?',
            'categories': {
                'beef': {
                    'id': '3015',
                    'question': 'How will you be preparing the beef?  Any spices or sauces you will be using?',
                    'categories': {
                        'herbs': {
                            'id': '3019'
                        },
                        'hot spices': {
                            'id': '3020'
                        },
                        'mushroom': {
                            'id': '3021'
                        },
                        'stew': {
                            'id': '3022'
                        },
                        'barbeque': {
                            'id': '3023'
                        },
                        'burgers': {
                            'id': '3024'
                        }
                    }
                },
                'lamb': {
                    'id': '3016',
                    'question': 'Anything you will be having with the lamb?',
                    'categories': {
                        'herbs': {
                            'id': '3025'
                        },
                        'hot spices': {
                            'id': '3026'
                        }
                    }
                },
                'pork': {
                    'id': '3017',
                    'question': 'How will you be preparing the pork?  Any spices or sauces you will be using?',
                    'categories': {
                        'herbs': {
                            'id': '3027'
                        },
                        'hot spices': {
                            'id': '3028'
                        },
                        'mushroom': {
                            'id': '3029'
                        },
                        'sausage': {
                            'id': '3030'
                        },
                        'tenderloin': {
                            'id': '3031'
                        },
                        'barbeque': {
                            'id': '3032'
                        },
                        'breaded': {
                            'id': '3033'
                        },
                        'fruit': {
                            'id': '3034'
                        }
                    }
                },
                'veal': {
                    'id': '3018',
                    'question': 'How will you be preparing the pork?  Any spices or sauces you will be using?',
                    'categories': {
                        'herbs': {
                            'id': '3035'
                        },
                        'lemon': {
                            'id': '3036'
                        },
                        'citrus': {
                            'id': '3036'
                        },
                        'lemon or citrus': {
                            'id': '3036'
                        },
                        'mushroom': {
                            'id': '3037'
                        },
                        'breaded': {
                            'id': '3038'
                        },
                        'chops': {
                            'id': '3039'
                        }
                    }
                }
            }
        },
        'cheese': {
            'id': '3009',
            'question': 'What kind of cheese do you have in mind?',
            'categories': {
                'blue': {
                    'id': '3040'
                },
                'cheddar': {
                    'id': '3041'
                },
                'creamy': {
                    'id': '3042'
                },
                'goat': {
                    'id': '3043'
                },
                'hard': {
                    'id': '3044'
                },
                'semi-firm': {
                    'id': '3045'
                },
                'stinky': {
                    'id': '3046'
                }
            }
        },
        'dessert': {
            'id': '3010',
            'question': 'What kind of dessert will you be having?',
            'categories': {
                'berries': {
                    'id': '3047'
                },
                'chocolate': {
                    'id': '3048'
                },
                'cream': {
                    'id': '3049'
                },
                'custard': {
                    'id': '3049'
                },
                'cream or custard': {
                    'id': '3049'
                },
                'lemon': {
                    'id': '3050'
                }
            }
        },
        'pasta and grains': {
            'id': '3012',
            'question': 'What kind of pasta do you have in mind?',
            'categories': {
                'lasagne': {
                    'id': '3055',
                    'question': 'What kind of lasagne do you plan on having?',
                    'categories': {
                        'meat': {
                            'id': '3060'
                        },
                        'vegetable': {
                            'id': '3061'
                        }
                    }
                },
                'paella': {
                    'id': '3056'
                },
                'pasta': {
                    'id': '3057',
                    'question': 'What do you plan on having with the pasta?',
                    'categories': {
                        'meat': {
                            'id': '3067'
                        },
                        'mushroom': {
                            'id': '3068'
                        },
                        'pesto': {
                            'id': '3069'
                        },
                        'tomato-base': {
                            'id': '3070'
                        },
                        'vegetable': {
                            'id': '3071'
                        },
                        'white sauce': {
                            'id': '3072'
                        },
                        'cream-based': {
                            'id': '3073'
                        }
                    }
                },
                'pizza': {
                    'id': '3058',
                    'question': 'What will be on the pizza?',
                    'categories': {
                        'meat': {
                            'id': '3062'
                        },
                        'vegetable': {
                            'id': '3063'
                        }
                    }
                },
                'risotto': {
                    'id': '3059',
                    'question': 'Any specific kind of risotto in mind?',
                    'categories': {
                        'mushroom': {
                            'id': '3064'
                        },
                        'plain': {
                            'id': '3065'
                        },
                        'primavera': {
                            'id': '3066'
                        }
                    }
                }
            }
        },
        'poultry': {
            'id': '3013',
            'question': 'Anything in specific?',
            'categories': {
                'cassoulet': {
                    'id': '3074'
                },
                'chicken': {
                    'id': '3075',
                    'question': 'How will you be preparing the chicken?  Any spices or sauces you will be using?',
                    'categories': {
                        'herbs': {
                            'id': '3078'
                        },
                        'lemon': {
                            'id': '3079'
                        },
                        'citrus': {
                            'id': '3079'
                        },
                        'lemon or citrus': {
                            'id': '3079'
                        },
                        'mushroom': {
                            'id': '3080'
                        },
                        'mustard': {
                            'id': '3081'
                        },
                        'spicy': {
                            'id': '3082'
                        },
                        'barbeque': {
                            'id': '3083'
                        },
                        'cream-based': {
                            'id': '3084'
                        },
                        'fried': {
                            'id': '3085'
                        }
                    }
                },
                'duck': {
                    'id': '3076',
                    'question': 'How will you be preparing the duck?',
                    'categories': {
                        'seared': {
                            'id': '3086'
                        },
                        'confit': {
                            'id': '3087'
                        },
                        'fois gras': {
                            'id': '3088'
                        },
                        'fruit': {
                            'id': '3089'
                        }
                    }
                },
                'turkey': {
                    'id': '3077',
                    'question': 'How will you be preparing the turkey?',
                    'categories': {
                        'lemon': {
                            'id': '3090'
                        },
                        'roasted': {
                            'id': '3091'
                        },
                        'breaded': {
                            'id': '3092'
                        }
                    }
                }
            }
        },
        'seafood': {
            'id': '3014',
            'question': 'What kind of seafood do you have in mind?',
            'categories': {
                'crab': {
                    'id': '3093',
                    'question': 'How will you be having the crab?',
                    'categories': {
                        'soft shelled': {
                            'id': '3102'
                        },
                        'spicy': {
                            'id': '3103'
                        },
                        'butter': {
                            'id': '3104'
                        },
                        'crab cakes': {
                            'id': '3105'
                        }
                    }
                },
                'lobster': {
                    'id': '3094',
                    'question': 'Do you plan on having the lobster with butter?',
                    'categories': {
                        'butter': {
                            'id': '3106'
                        }
                    }
                },
                'oysters': {
                    'id': '3095'
                },
                'salmon': {
                    'id': '3096',
                    'question': 'How will you be preparing the salmon?',
                    'categories': {
                        'herbs': {
                            'id': '3107'
                        },
                        'mustard': {
                            'id': '3108'
                        },
                        'grilled': {
                            'id': '3109'
                        }
                    }
                },
                'scallops': {
                    'id': '3097',
                    'question': 'How will you prepare the scallops?',
                    'categories': {
                        'herbs': {
                            'id': '3110'
                        },
                        'lemon': {
                            'id': '3111'
                        },
                        'citrus': {
                            'id': '3111'
                        },
                        'lemon or citrus': {
                            'id': '3111'
                        },
                        'butter': {
                            'id': '3112'
                        }
                    }
                },
                'shrimp': {
                    'id': '3098',
                    'question': 'What will you be having with the shrimp?',
                    'categories': {
                        'lemon': {
                            'id': '3113'
                        },
                        'citrus': {
                            'id': '3113'
                        },
                        'lemon or citrus': {
                            'id': '3113'
                        },
                        'herbs': {
                            'id': '3114'
                        }
                    }
                },
                'sushi': {
                    'id': '3099'
                },
                'tuna': {
                    'id': '3100',
                    'question': 'How will you be preparing the tuna?',
                    'categories': {
                        'seared': {
                            'id': '3115'
                        },
                        'spicy': {
                            'id': '3116'
                        }
                    }
                },
                'white fish': {
                    'id': '3101',
                    'question': 'How will you be preparing the white fish?  Any spices or sauces you will be using?',
                    'categories': {
                        'herbs': {
                            'id': '3117'
                        },
                        'hot spices': {
                            'id': '3118'
                        },
                        'lemon': {
                            'id': '3119'
                        },
                        'citrus': {
                            'id': '3119'
                        },
                        'lemon or citrus': {
                            'id': '3119'
                        },
                        'stew': {
                            'id': '3120'
                        },
                        'fish tacos': {
                            'id': '3121'
                        },
                        'fried': {
                            'id': '3122'
                        }
                    }
                }
            }
        }
    }
}
