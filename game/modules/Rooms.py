def get_map():
	return {
			'outside' : {
				'description' : """The air is still has the memory of winter about it. The late spring eve 
is framed by the orangey glow of the sun sinking into the horizon. The air 
is thick and pungent with the smoke of many peat fires from all the inns
along south london road. The road is cobble stone. The cobbles are slick with 
the muck of the many horses and pack mules that past this way bound for 
Canterbury.""",
				'actions' : {
					'move north' : 'tabard exterior'
				}
			},
			'tabard exterior' : {
				'description' : """
	The Tabard stands before you. It's marked by its swinging sign board,
	gaudily done in the Abbot of Hyde's colors. The greatest of the 
	great inns all shoved up on each other along South London road. It
	dwarves its smalller competitors like the Bull and Feather. It's 
	Southwark's finest inn as all know it. Tonight it's full to bursting 
	with pilgrims bound Canterbury way. The mud and daub structure with 
	exposed timbers stands regally and beckons entry to all who pass by. 
	""",
				'actions' : {
					'move north' : 'tabard interior'
				}
			},
			'tabard interior' : {
			 	'description' : """
	The inn is bright and lively on this spring eve. The rich timbre of 
	drunken song and clink of earth-waren tankards rebound off the walls. 
	The peppery smell of many unwashed bodies, and clean horse sweat pervade the
	air.
	""",		
				'actions' : { 
					'move north' : 'hearth',
					'move west' : 'bar'
				}
			},
			'bar' : {
				'description' : """
	The bar is a long oaken trestle that stretches along the back of the inn
	proper. There are a few stools. Perched on one of them, is scholarly fellow
	with an impish grin, and a merry twinkle in his eye. He's strategically
	positioned himself near the taps.
	""",		'actions' : {
					"north" : 'outside',
					"west" : 'tabard exterior',
					"east" : 'tabard interior'
				}
			}
	}

	# after we talk to chaucer there will be new 
	# options