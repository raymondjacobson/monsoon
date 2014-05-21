//
//  AppDelegate.h
//  monsoon-cocoa
//
//  Created by Raymond Jacobson on 5/20/14.
//  Copyright (c) 2014 raymondjacobson. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface AppDelegate : NSObject <NSApplicationDelegate> {
    IBOutlet NSMenu *statusMenu;
    NSStatusItem *statusItem;
    NSImage *statusImage;
}

- (IBAction)put:(id)sender;
- (IBAction)grab:(id)sender;
- (IBAction)quit:(id)sender;

@end
