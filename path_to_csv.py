#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import math
import inkex
import simplepath
import simplestyle
import cubicsuperpath
import simpletransform


__version__ = '0.1'

inkex.localize()

### Main function subclasses the inkex.Effect class
class Myextension(inkex.Effect):
    
    def __init__(self):
        inkex.Effect.__init__(self) # initialize the super class
        self.OptionParser.add_option("-d", "--dotsize",
                        action="store", type="string",
                        dest="dotsize", default="5",
                        help="Size of the dots placed at path nodes")
        self.OptionParser.add_option("-f", "--fontsize",
                        action="store", type="string",
                        dest="fontsize", default="2",
                        help="Size of node label numbers")
        self.OptionParser.add_option("-m", "--makedots",
                        action="store", type="inkbool",
                        dest="makedots", default=True,
                        help="Is show node point dots")
        self.OptionParser.add_option("-p", "--savepath",
                        action="store", type="string",
                        dest="savepath", default="C:\\Inkscape\\export_csv",
                        help="export csv to path")
        self.OptionParser.add_option("-o", "--openpath",
                        action="store", type="inkbool",
                        dest="openpath", default=True,
                        help="open path when export csv")
    def effect(self):
        selection = self.selected
        if (selection):
            # 获得选择的项目
            for _id, node in selection.iteritems():
                if node.tag == inkex.addNS('path','svg'):
                    if self.options.makedots:
                        self.addDot(node)
                    self.getDot(node,_id)
        else:
            inkex.errormsg("Please select an object.")
    def separateLastAndFirst(self, p):
        # Separate the last and first dot if they are togheter
        lastDot = -1
        if p[lastDot][1] == []: lastDot = -2
        if round(p[lastDot][1][-2]) == round(p[0][1][-2]) and \
                round(p[lastDot][1][-1]) == round(p[0][1][-1]):
                x1 = p[lastDot][1][-2]
                y1 = p[lastDot][1][-1]
                x2 = p[lastDot-1][1][-2]
                y2 = p[lastDot-1][1][-1]
                dx = abs( max(x1,x2) - min(x1,x2) )
                dy = abs( max(y1,y2) - min(y1,y2) )
                dist = math.sqrt( dx**2 + dy**2 )
                x = dx/dist
                y = dy/dist
                if x1 > x2: x *= -1
                if y1 > y2: y *= -1
                p[lastDot][1][-2] += x * self.unittouu(self.options.dotsize)
                p[lastDot][1][-1] += y * self.unittouu(self.options.dotsize)

    def addDot(self, node):
        self.group = inkex.etree.SubElement( node.getparent(), inkex.addNS('g','svg') )
        self.dotGroup = inkex.etree.SubElement( self.group, inkex.addNS('g','svg') )
        self.numGroup = inkex.etree.SubElement( self.group, inkex.addNS('g','svg') )
        
        try:
            t = node.get('transform')
            self.group.set('transform', t)
        except:
            pass

        style = simplestyle.formatStyle({ 'stroke': 'none', 'fill': '#000' })
        a = []
        p = simplepath.parsePath(node.get('d'))

        self.separateLastAndFirst(p)

        num = 0
        for cmd,params in p:
            if cmd != 'Z' and cmd != 'z':
                dot_att = {
                  'style': style,
                  'r':  str( self.unittouu(self.options.dotsize) / 2 ),
                  'cx': str( params[-2] ),
                  'cy': str( params[-1] )
                }
                inkex.etree.SubElement(
                  self.dotGroup,
                  inkex.addNS('circle','svg'),
                  dot_att )
                self.addText(
                  self.numGroup,
                  params[-2] + ( self.unittouu(self.options.dotsize) / 2 ),
                  params[-1] - ( self.unittouu(self.options.dotsize) / 2 ),
                  num )
                num += 1

    def addText(self,node,x,y,text):
                new = inkex.etree.SubElement(node,inkex.addNS('text','svg'))
                s = {'font-size': self.unittouu(self.options.fontsize), 'fill-opacity': '1.0', 'stroke': 'none',
                    'font-weight': 'normal', 'font-style': 'normal', 'fill': '#999'}
                new.set('style', simplestyle.formatStyle(s))
                new.set('x', str(x))
                new.set('y', str(y))
                new.text = str(text)

    def getDot(self, node,_id):
        a = []
        p = simplepath.parsePath(node.get('d'))
        self.separateLastAndFirst(p)
        num = 0
        nodes=""
        for cmd,params in p:
            if cmd != 'Z' and cmd != 'z':
                nodes+='"{0}","{1:.3f}","{2:.3f}",","\n'.format(num,params[-2],params[-1])
                num += 1
        self.saveCSV(_id,nodes)
    def saveCSV(self,file,content):
        if os.path.exists(self.options.savepath)==False:
            os.makedirs(self.options.savepath)
        _file=self.options.savepath+'/'+file+'.csv'
        f=open(_file,'w+')
        f.write('"Index","X (mm)","Y (mm)","Arc Angle (Neg = CW)"\n')
        f.write(content)
        f.close()
        if self.options.openpath:
            os.startfile(self.options.savepath)
if __name__ == '__main__':
    e = Myextension()
    e.affect()