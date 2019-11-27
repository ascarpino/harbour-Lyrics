/*
  The MIT License (MIT)

  Copyright (c) 2015 Andrea Scarpino <me@andreascarpino.it>

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
*/

#ifndef PROVIDER_H
#define PROVIDER_H

#include <QObject>
#include <QString>

class Lyric;

class Provider : public QObject
{
    Q_OBJECT
public:
    virtual ~Provider();

    virtual void getLyric(const QString &artist, const QString &song) = 0;

protected:
    Provider(QObject *parent = 0);

Q_SIGNALS:
    void lyricFetched(Lyric *lyric, const bool &found);

};

Q_DECLARE_INTERFACE(Provider, "Provider")

#endif // PROVIDER_H
