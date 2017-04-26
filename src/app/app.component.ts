import { Component } from '@angular/core';
import { TweetsComponent } from './components/tweets/tweets'
import { TweetService } from './services/tweetService'

@Component({
  selector: 'my-app',
  template: `<nav>
                <h1>{{name}}!</h1>
            </nav>
            <tweets></tweets>`,
  styles: [
      'nav {width: 100%; height:15vh; position: fixed; top: 0vh; background-color: #336699; display: inline-flex; z-index: 10;}',
      'h1 {color: white; font-size: 250%; align-self: flex-end; margin: 15px;}',
      'tweets { position: relative; top: 15vh; }'
  ],
  directives: [TweetsComponent],
  providers: [TweetService]
})

export class AppComponent {
  name:string = 'Twitter Playoffs';

  constructor() {}
}
