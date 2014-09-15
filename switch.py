def say(myParam='default'):
	print "YES! %s" % myParam

{
	"1": say,
	"2": say,
	"3": say,
	"4": say
}[raw_input("num ? ")]()