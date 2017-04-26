import { Component, OnInit } from '@angular/core';
import { TweetService } from '../../services/tweetService'

@Component({
  selector: 'tweets',
  template: `<ul><li *ngFor="let tweet of tweets">{{tweet.text}}</li></ul>`
})
export class TweetsComponent implements OnInit {
  tweets: any[];
  error: any;

  constructor(private tweetService: TweetService) { }

  getTweets() {
    this.tweetService
        .getTweets()
        // .then(tweets => {console.log(tweets)})
        .then(tweets => this.tweets = tweets)
        .catch(error => this.error = error);
  }

  ngOnInit() {
    this.getTweets();
  }
}