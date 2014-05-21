//
//  AppDelegate.m
//  monsoon-cocoa
//
//  Created by Raymond Jacobson on 5/20/14.
//  Copyright (c) 2014 raymondjacobson. All rights reserved.
//

#import "AppDelegate.h"

@implementation AppDelegate

- (void)awakeFromNib {
    statusItem = [[NSStatusBar systemStatusBar] statusItemWithLength:NSVariableStatusItemLength];
    NSBundle *bundle = [NSBundle mainBundle];
    statusImage = [[NSImage alloc] initWithContentsOfFile:[bundle pathForResource:@"icon" ofType:@"png"]];
    
    [statusItem setImage:statusImage];
    [statusItem setMenu:statusMenu];
    [statusItem setToolTip:@"Vacant"];
    [statusItem setHighlightMode:YES];
}

- (IBAction)put:(id)sender {
    NSLog(@"putting a file");
}

- (IBAction)grab:(id)sender {
    NSLog(@"grabbing a file");
}

- (IBAction)quit:(id)sender {
    [NSApp terminate:nil];
}

@end
