import pgf
import wordnet as w
from wordnet.api import *
from nlg.util import *

def render(db, lexeme, cnc, entity):
	yield "<div class='infobox'>"
	# show the flag and the coat of arms if available
	for media,qual in get_medias("P18",entity):
		yield "<img src='"+escape(media)+"' width=250/>"
		break
	yield "</div>"

	country_qids = get_items("P17", entity)
	if country_qids:
		cn = mkCN(mkCN(w.city_1_N),mkAdv(w.in_1_Prep,mkNP(pgf.ExprFun(get_lex_fun(db, country_qids[0][0])))))
	else:
		cn = mkCN(w.city_1_N)

	phr=mkPhr(mkUtt(mkS(mkCl(mkNP(lexeme),mkNP(aSg_Det,cn)))),fullStopPunct)
	yield "<p>"+escape(cnc.linearize(phr))+"</p>"
