# - *-coding: utf- 8 - *-

class Jobs:

	all_vars = {}

	def set_var(self, Vars):
		for var in Vars:
			self.all_vars[var] = Vars[var]

	def get_var(self, VarKey):
		print self.all_vars[VarKey]

	def set_job (self, newJobs = list()):
		if len(newJobs) > 0:
			for newJob in newJobs:
				if newJob not in self.all_vars['jobs']:
					self.all_vars['jobs'].append(newJob)

	def get_jobs(self):
		jobIdx = 1
		for job in sorted(self.all_vars['jobs']):
			print "%d) %s" % (jobIdx, job)
			jobIdx += 1

class ClassName(Jobs):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(Jobs, self).__init__()
		self.arg = arg
		

#test
jobs = Jobs()
jobs.set_var({'jobs':list()})
jobs.set_job(['web developer', 'web designer'])
jobs.get_var('jobs')
