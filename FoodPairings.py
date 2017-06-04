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
    'seafood+crab+spicey': '7155+3103',
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


foodPairings = {
    'meat': {
        'id': '7155+3008',
        'categories': {
            'beef': {
                'id': '7155+3015',
                'categories': {
                    'herbs': {

                    },
                    'hot spices': {

                    },
                    'mushroom': {

                    },
                    'stew': {

                    },
                    'bbq': {
                    
                    },
                    'burgers': {

                    },
                }
            },
            'lamb': {

            },
            'pork': {

            },
            'veal': {

            },
        }
    },
    'cheese': {
        'id': '7155+3009'

    },
    'dessert': {

    },
    'pasta and grains': {

    },
    'poultry': {

    },
    'seafood': {

    }
}
